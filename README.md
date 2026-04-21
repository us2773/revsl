# revsl

クリップボードのテキストのバックスラッシュをスラッシュに置き換えるCLIアプリ

Windowsで開発する際、コピーしたpathの区切り文字はバックスラッシュまたは¥で表記されるが、ソースコード上ではスラッシュで表記したい、といった場合にお使いください。

```powershell
> revsl
clipboard: C:\Users\user\path\to\your\directory\revsl.exe
new clipboard: C:/Users/user/path/to/your/directory/revsl.exe
```

そのままクリップボードに置換されたテキストがコピーされます。

# 使い方

Releaseからexeファイルをダウンロードし、パスを通してください。
