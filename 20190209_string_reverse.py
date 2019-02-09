def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse
  # 思路1：想要取得一个string的倒叙则只需要将[0,1,2,3...len(word)]倒叙成[len(word)-1,len(word)-2....-1](而实现数列位置倒叙的方式就是range（len(word)-1,-1 -1）
  # 思路2：对于数组list,可以用append()函数在后续添加元素。但是对于字符串想要后续添加字母，却无法使用append（）函数，因为append（）只能作用于数组list。对于字符串string，则应该用for循环，然后 a += "string" 来实现。
  