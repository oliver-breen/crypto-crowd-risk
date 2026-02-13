# OWASP 2025 Cryptography Guidelines

This document outlines the OWASP 2025 cryptography guidelines that this tool implements.

## Overview

OWASP (Open Web Application Security Project) provides comprehensive guidance on secure cryptographic practices. The 2025 guidelines reflect modern threats including:

- Advances in cryptanalysis
- Quantum computing threats
- Increased computational power
- Lessons learned from past vulnerabilities

## Key Principles

### 1. Use Strong, Modern Algorithms

**Approved Symmetric Encryption:**
- ✅ AES-256-GCM (Authenticated Encryption with Associated Data)
- ✅ ChaCha20-Poly1305
- ❌ DES, 3DES, RC4 (Deprecated)

**Approved Asymmetric Encryption:**
- ✅ RSA with 4096-bit keys minimum
- ✅ ECDSA with P-384 or P-521 curves
- ✅ Ed25519 (EdDSA)
- ❌ RSA-2048 or smaller (Deprecated for new systems)
- ❌ RSA-1024 (Critically insecure)

**Approved Hash Functions:**
- ✅ SHA-256, SHA-384, SHA-512
- ✅ SHA3-256, SHA3-512
- ❌ MD5 (Broken)
- ❌ SHA-1 (Broken)

### 2. Key Length Requirements

Minimum key lengths for OWASP 2025 compliance:

| Algorithm Type | Minimum Key Length | Recommended |
|----------------|-------------------|-------------|
| Symmetric (AES) | 256 bits | 256 bits |
| RSA | 4096 bits | 4096 bits |
| ECC | 384 bits (P-384) | 521 bits (P-521) |
| HMAC | 256 bits | 384+ bits |

### 3. Quantum Resistance Planning

**OWASP 2025 emphasizes preparing for quantum threats:**

- **Current Status**: Most public-key cryptography (RSA, ECC) is vulnerable to quantum attacks via Shor's algorithm
- **Timeline**: Quantum computers capable of breaking current crypto may arrive within 10-20 years
- **Action Required**: Begin planning migration to post-quantum cryptography (PQC)

**Quantum Impact:**

| Algorithm | Quantum Vulnerability | Security Level (Quantum) |
|-----------|----------------------|-------------------------|
| RSA-2048 | HIGH - Shor's algorithm | Broken |
| RSA-4096 | HIGH - Shor's algorithm | Broken |
| ECC P-256 | HIGH - Shor's algorithm | Broken |
| AES-128 | MEDIUM - Grover's algorithm | ~64-bit |
| AES-256 | MEDIUM - Grover's algorithm | ~128-bit |
| SHA-256 | LOW - Grover's algorithm | ~128-bit |

**Post-Quantum Cryptography (PQC) Options:**
- CRYSTALS-Kyber (key encapsulation)
- CRYSTALS-Dilithium (digital signatures)
- Falcon (digital signatures)
- Hybrid approaches (classical + PQC)

### 4. Cryptographic Agility

**Definition**: The ability to quickly switch cryptographic algorithms when vulnerabilities are discovered.

**Requirements:**
- Support for multiple algorithm versions
- Clear upgrade paths
- Governance processes for security updates
- Backward compatibility during transitions

**Implementation:**
```python
# Example of algorithm versioning
{
    "algorithm_version": "v2",
    "cipher": "AES-256-GCM",
    "fallback": ["AES-256-CBC"],  # Deprecated but supported
    "future": ["post-quantum-hybrid"]  # Planned upgrade
}
```

### 5. Random Number Generation

**Requirements:**
- Use cryptographically secure random number generators (CSPRNG)
- Never use `rand()` or `Math.random()` for security purposes
- Properly seed random number generators

**Approved Sources:**
- `/dev/urandom` (Linux/Unix)
- `CryptGenRandom` (Windows)
- `secrets` module (Python 3.6+)
- `crypto.randomBytes()` (Node.js)

### 6. Key Management

**OWASP 2025 Key Management Principles:**

1. **Key Generation**
   - Use cryptographic libraries, never implement yourself
   - Generate keys with sufficient entropy
   - Use appropriate key derivation functions (KDFs)

2. **Key Storage**
   - Never store keys in plaintext
   - Use hardware security modules (HSMs) for high-value keys
   - Implement key encryption keys (KEK) pattern
   - Consider key splitting for multi-party scenarios

3. **Key Rotation**
   - Rotate keys periodically
   - Implement versioning for smooth transitions
   - Archive old keys for decryption of historical data

4. **Key Destruction**
   - Securely erase keys when no longer needed
   - Multiple overwrites for key material
   - Consider hardware secure deletion

### 7. Secure Hashing

**Password Hashing:**
- ✅ Argon2id (Winner of Password Hashing Competition)
- ✅ bcrypt (with cost factor ≥ 12)
- ✅ scrypt
- ❌ Plain SHA-256/SHA-512 (too fast)
- ❌ MD5 (broken)

**Data Integrity:**
- Use HMAC (Hash-based Message Authentication Code)
- Minimum HMAC key length: 256 bits
- Combine with authenticated encryption when possible

### 8. Certificate and PKI Best Practices

**Certificate Requirements:**
- Minimum 2048-bit RSA (4096-bit recommended)
- Use SHA-256 or SHA-384 for signatures
- Implement Certificate Transparency
- Short validity periods (≤ 1 year for web)

**TLS/SSL:**
- TLS 1.3 preferred
- TLS 1.2 minimum (with strong cipher suites)
- Disable TLS 1.0 and 1.1
- Use perfect forward secrecy (PFS)

### 9. Cryptocurrency-Specific Guidelines

**Blockchain Cryptography:**
- Bitcoin: ECDSA with secp256k1, SHA-256
- Ethereum: ECDSA with secp256k1, Keccak-256
- Consider quantum-resistant signatures for long-term value storage

**Wallet Security:**
- Use BIP-39 for mnemonic generation
- Implement BIP-44 for hierarchical deterministic (HD) wallets
- Add passphrase protection (BIP-39 extension)
- Consider multi-signature schemes

**Transaction Signing:**
- Use deterministic nonce generation (RFC 6979)
- Implement signature malleability protection
- Constant-time operations to prevent side-channel attacks
- Validate all signatures on chain

### 10. Compliance Checklist

Use this checklist to verify OWASP 2025 compliance:

**Encryption:**
- [ ] Using AES-256-GCM or ChaCha20-Poly1305
- [ ] No use of DES, 3DES, or RC4
- [ ] Minimum 256-bit symmetric keys

**Asymmetric Crypto:**
- [ ] RSA keys are 4096 bits or larger
- [ ] ECC uses P-384 or stronger curves
- [ ] No RSA-2048 in new implementations

**Hashing:**
- [ ] Using SHA-256 or stronger
- [ ] No MD5 or SHA-1
- [ ] Proper salt for password hashing
- [ ] Using Argon2id/bcrypt/scrypt for passwords

**Random Number Generation:**
- [ ] Using CSPRNG (not pseudo-random)
- [ ] Proper entropy sources

**Key Management:**
- [ ] Keys not stored in plaintext
- [ ] Key rotation implemented
- [ ] Secure key destruction process

**Quantum Preparedness:**
- [ ] Aware of quantum threats
- [ ] Planning for PQC migration
- [ ] Monitoring NIST PQC standards

**Cryptographic Agility:**
- [ ] Algorithm versioning supported
- [ ] Upgrade mechanism exists
- [ ] Governance process defined

## Implementation in Crypto Crowd Risk Tool

This tool implements these guidelines through:

1. **OWASPCryptoChecker**: Validates algorithms and key lengths
2. **CryptoRiskAnalyzer**: Assesses cryptocurrency-specific risks
3. **MarketConditionAnalyzer**: Evaluates economic security
4. **Automated Compliance Reports**: Generates actionable findings

## Resources

- [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- [OWASP Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html)
- [NIST Special Publication 800-175B](https://csrc.nist.gov/publications/detail/sp/800-175b/final)
- [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)

## Updates and Maintenance

Cryptographic standards evolve constantly. This tool should be updated as:
- New OWASP guidelines are released
- NIST finalizes PQC standards
- New vulnerabilities are discovered
- Industry best practices change

---

**Note**: These guidelines represent a synthesis of OWASP recommendations, NIST standards, and cryptocurrency industry best practices as of 2025. Always consult official sources for the most current guidance.
