"""Package version and the simplex-chat-libs release it loads.

Written by scripts/ci/packages_release.py: the release PR bumps the version
and pins new library releases with the SHA-256 of their assets.
"""

__version__ = "7.1.0b6.post4"  # PEP 440 — read by hatchling for wheel metadata
LIBS_RELEASE = "core-7.1.0.13"  # simplex-chat-libs release tag
LIBS_SHA256 = {
    "simplex-chat-libs-linux-aarch64.zip": "bd3b3f2f82122c05aeec158309eabdb41514c9954fdf8979f302aa51000c4fd7",
    "simplex-chat-libs-linux-x86_64-postgres.zip": "447be405e8ffe3742bae87b08191c532c8c6a1fce5b15dfc7ff174c3aac16531",
    "simplex-chat-libs-linux-x86_64.zip": "d225628fb83c13ee9c3c5547afa0427a7e04d39f12757a9a33175ff904372e05",
    "simplex-chat-libs-macos-aarch64.zip": "af8a838f0b54a4b3ed92dc64382994e23b8c599c09454af9ecce06cd077f97db",
    "simplex-chat-libs-macos-x86_64.zip": "8066e34d25dcebd3bd1f792f581e375f0e529e68410ed202854e0a02b8d8e802",
    "simplex-chat-libs-windows-x86_64.zip": "60400d9e9b22f7bae91017b21b66bc1fb65ca833a5795698626e5aa12c8dfc20",
}
