# Wrap the artifact source into a standalone app/index.html for GitHub Pages.
import sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src).read()
s=s.replace('<title>ブルベクエスト北海道</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n','')
head='''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>ブルベクエスト北海道</title>
<meta name="description" content="AJ北海道・ランドヌール札幌・AJたまがわの2026年ブルベ日程で1シーズンを過ごす、ファミコン風ロードバイクゲーム。">
<link rel="icon" href="../assets/favicon.ico">
<link rel="apple-touch-icon" href="../assets/icon.png">
'''
i=s.index('<div id="app">')
open(dst,'w').write(head+s[:i]+'</head>\n<body>\n'+s[i:]+'\n</body>\n</html>\n')
