## 문제: 자연수 뒤집어 배열로 만들기 

자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

## Java

### My Solution 
```java
class Solution {
  public int[] solution(long n) {      
      int[] answer = new int[Long.toString(n).length()];
      int i=0;
      while(n>0){
        answer[i++]=(int)(n%10);
        n=n/10;
      }
      return answer;
  }
}
```

### Best solution 
```java

class Solution {
  public int[] solution(long n) {
      String a = "" + n;
        int[] answer = new int[a.length()];
        int cnt=0;

        while(n>0) {
            answer[cnt]=(int)(n%10);
            n/=10;
            System.out.println(n);
            cnt++;
        }
      return answer;
  }
}

```



<bold> source: https://programmers.co.kr/learn/courses/30/lessons/12932?language=java </bold>
