from setuptools import setup, find_packages

setup(
    name="constitutional-ai",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # 这里可以添加依赖包
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A framework for provably reliable LLM outputs",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://gitee.com/your-username/Constitutional-AI",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
)
