from setuptools import setup, find_packages

setup(
    name="jianyingdraft",
    version="0.1.1",
    author="doumai",
    description="轻量、灵活、易上手的Python剪映草稿生成及导出工具，构建全自动化视频剪辑/混剪流水线",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/doumai-0130/jianyingdraft",
    packages=find_packages(),
    package_data={
        'jianyingdraft': ['draft_content_template.json']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Multimedia :: Video"
    ],
    python_requires='>=3.8',
    install_requires=[
        "pymediainfo",
        "imageio"
    ],
)
