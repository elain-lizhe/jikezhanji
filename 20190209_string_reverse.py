def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse
  # 思路：想要取得一个string的倒叙则只需要将[0,1,2,3...len(word)]倒叙成[len(word)-1,len(word)-2....-1](而实现数列位置倒叙的方式就是range（len(word)-1,-1 -1）