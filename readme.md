# PixelProof

PixelProof is a prototype system for **cryptographically verifying the authenticity and integrity of digital images**. It allows an image to be signed by its creator and later verified to detect whether the image has been modified.

The goal of this project is to demonstrate how **hashing and digital signatures** can be used to prove that an image has not been altered after it was created.

This project is a **security and backend engineering prototype** focused on media authenticity.

---

# Problem

Digital images can easily be modified using editing tools or AI systems. Once modified, it becomes difficult to determine:

* whether an image is original
* whether it has been altered
* who created it

Traditional formats such as JPG or PNG provide **no built-in authenticity verification**.

PixelProof addresses this by introducing a **signed image container** that allows anyone to verify whether an image has been tampered with.

---

# Solution

PixelProof signs an image using **cryptographic hashing and digital signatures**.

When an image is signed:

1. A cryptographic hash of the image is generated.
2. The hash is digitally signed using the creator's private key.
3. The image, metadata, and signature are stored in a secure container.

During verification, the system recomputes the image hash and validates the digital signature.

If the image has been modified, the hash changes and verification fails.

---

# How It Works

## Signing Process

1. The original image is uploaded.
2. The system computes a SHA-256 hash of the image bytes.
3. Metadata describing the image is generated.
4. The hash is signed using the creator’s private key.
5. A secure container file is created.

Process flow:

```
Image
 ↓
SHA256 Hash
 ↓
Digital Signature
 ↓
Secure Container (.ppimg)
```

---

## Verification Process

1. The secure container is opened.
2. The image, metadata, and signature are extracted.
3. The image hash is recalculated.
4. The recalculated hash is compared with the stored hash.
5. The signature is verified using the creator’s public key.

Verification logic:

```
if recalculated_hash != stored_hash:
    image was modified

else if signature invalid:
    signature forged

else:
    image authentic
```

---

# Container Format

PixelProof uses a simple container format for storing signed images.

Example file:

```
photo.ppimg
```

Internal structure:

```
photo.ppimg
│
├── image.jpg
├── metadata.json
└── signature.sig
```

### image.jpg

The original image file.

### metadata.json

Stores information about the image and its hash.

Example:

```json
{
  "creator": "Kedar",
  "timestamp": "2026-03-08T12:00:00",
  "hash_algorithm": "SHA256",
  "image_hash": "9af31b7c..."
}
```

### signature.sig

A digital signature generated from the image hash using the creator’s private key.

---

# Security Model

PixelProof provides **integrity and authenticity verification**.

The system guarantees:

* Any pixel modification changes the image hash.
* Only the creator’s private key can generate a valid signature.
* Anyone with the public key can verify authenticity.

The system does **not prevent image copying or screenshots**. Instead, it ensures that **modified images cannot be falsely presented as authentic originals**.

---

# Example Scenario

### Original Image

A creator signs an image using PixelProof.

Verification result:

```
Authentic Image
Signature Valid
```

### Edited Image

The image is modified using an editor.

Verification result:

```
Tampering Detected
Hash Mismatch
```

---

# Project Goals

This project aims to demonstrate:

* image integrity verification
* digital signature usage
* secure container design
* tamper detection for media files

The system acts as a **proof-of-concept for verifiable digital media**.

---

# Future Improvements

Possible extensions for this system include:

* invisible forensic watermarking
* AI-based deepfake detection
* provenance tracking
* public key registries
* browser extensions for automatic verification
* integration with media platforms

---

# Disclaimer

PixelProof is a **prototype system for demonstrating image authenticity verification concepts**. It does not completely prevent misuse of images but provides a mechanism to verify whether an image is original or modified.

---

# License

This project is intended for educational and research purposes.
