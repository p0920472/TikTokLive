import setuptools

# PyPi upload Command
# rm -r dist ; python setup.py sdist ; python -m twine upload dist/*

manifest: dict = {
    "name": "TikTokLive",
    "license": "MIT",
    "author": "Isaac Kogan",
    "version": "6.1.0",
    "email": "info@isaackogan.com"
}

if __name__ == '__main__':
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name=manifest["name"],
        packages=setuptools.find_packages(),
        version=manifest["version"],
        license=manifest["license"],
        description="TikTok Live Python Client",
        author=manifest["author"],
        author_email=manifest["email"],
        url="https://github.com/isaackogan/TikTokLive",
        long_description=long_description,
        long_description_content_type="text/markdown",
        download_url=f"https://github.com/isaackogan/TikTokLive/releases/tag/v{manifest['version']}",
        keywords=["tiktok", "tiktok live", "python3", "api", "unofficial"],
        install_requires=[
            "httpx>=0.25.0",
            "pyee>=9.0.4",
            "ffmpy>=0.3.0",
            "websockets_proxy>=0.1.0",
            "betterproto>=2.0.0b6",
            "async-timeout>=4.0.3",

            # Legacy-only requirements (to be removed)
            "mashumaro>=3.5",  # JSON Deserialization
            "protobuf3-to-dict>=0.1.5",
            "protobuf>=3.19.4",

        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Build Tools",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
        ]
    )
