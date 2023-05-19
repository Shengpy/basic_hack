a=5
b=";print('haha')#"
c="5"
result={}
code=compile(f'result={int(a)}{b}{int(c)}','<string>','exec')
exec(code,result)
print(result.get('result'))