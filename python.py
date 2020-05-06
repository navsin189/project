#!/usr/bin/python3
import os
import cgi
import subprocess

print("Content-type:text/html")
print()
x='''
<style>
.header {
  padding:0;
  text-align: center;
  font-family:courier;
  background: #eee9e9;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: right;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}


li a:hover:not(.active) {
  background-color: #eee9e9;
  color:Tomato;
}
.active{
background-color: #4CAF50;
}

.button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}
body{
        background-image:url('https://www.wallpaperswide.com/download/iron_man_comic_art-wallpaper-1366x768.jpg');
}

</style>
</head>
<body  background="/var/www/cgi-bin/ironman.jpg">
<div class="header">
  <h3>Python Online Compiler</h3>
</div>
<ul>
   <li><a class="active" href="#home">Home</a></li>
  <li><a href="https://www.instagram.com/mr.knight_13/?hl=en">Instagram</a></li>
  <li><a href="https://www.facebook.com/nhi.bataunga.kabhi" target=_blank>Facebook</a></li>
  <li><a href="https://www.linkedin.com/in/navsin189" target=_blank>LinkedIn</a></li>
</ul><br><br>
<form method=post>
<textarea row="5" cols="20"  placeholder="Write the code in the space provided" style="color:#008CBA;width:300px; height:300px;" name="code"></textarea>
<br>
<button type=submit value="submit" class="button">Run</button>
</form>

</body>
'''
print(x)
w=cgi.FieldStorage()
a=w.getvalue("code")
file1=open(r"/var/www/cgi-bin/op.py","w")
file1.writelines(a)
file1.close()
op=subprocess.getoutput("python3  /var/www/cgi-bin/op.py")
print("")
print("the output:\t",op)
d='''
<style>
.footer {
  padding:0;
  text-align: center;
  background: #ddd;
  font-family:courier;
  margin-top: 20px;
}
</style>
<form>
<div class="footer">
  <h3><b>Note:</b>The TextArea can be resized</h3>
</div>
</form>'''
print(d)
