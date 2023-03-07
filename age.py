driving = input('请问你有没有开过车')
if driving != '有' and driving != '没有':
    print('只能输入 有/没有')
    raise SystemExit

age = input('请问你的年龄?')
age = int(age)
if driving == '有':
    if age >= 18:#不能直接age>=18,因为接受input输入的数字默认为字符型，所以需要转换
        print('你通过测验了')
    else:
        print('奇怪，你怎么会有开过车')
elif driving == '没有':
    if age >= 18:
        print('你可以考驾照了啊，怎么还不去考')
    else:
        print('很好，再过几年就可以考驾照了')
