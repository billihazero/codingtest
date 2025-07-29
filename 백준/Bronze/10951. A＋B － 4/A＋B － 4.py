while True:
   try: 
      a,b = map(int, input().split(" "))
      print (a + b)
   #조건을 주지않아서 런타임 에러 발생
   except:
      break