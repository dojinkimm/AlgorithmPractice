## 문제: 정수 내림차순 구하기 

함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.



## Java

### My Solution 
```java
import java.util.*;

class Solution {
  public long solution(long n) {
      long answer = 0;
      char[] array=Long.toString(n).toCharArray();
      Arrays.sort(array);
     
      String reverse = new StringBuffer(new String(array)).reverse().toString();
      
      return Long.parseLong(reverse);
  }
}
```


### Best solution 
```java
  public int reverseInt(int n){

        String str = Integer.toString(n);
        char[] c = str.toCharArray();
        Arrays.sort(c);
        StringBuilder sb = new StringBuilder(new String(c,0,c.length));  
        return Integer.parseInt(((sb.reverse()).toString()));
    }

```

## Python

```python
def solution(n):
    answer = sorted(str(n), reverse=True)
    return int("".join(answer)) 
```




<bold> source: https://programmers.co.kr/learn/courses/30/lessons/12933?language=java </bold>
