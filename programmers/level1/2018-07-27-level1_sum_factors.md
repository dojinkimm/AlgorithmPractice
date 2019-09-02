## 문제: 약수의 합 구하기 

자연수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

입출력 예 #1
12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.


## Java

### My Solution 
```java
class Solution {
  public int solution(int n) {
      int answer = 0;
      for(int i=1;i<=n/2;i++){
          if(n%i==0)
              answer+=i;
      }
      
      return answer+n;
  }
}
```

### Best solution 
```java

  public int sumDivisor(int num) {
        int answer = 0;
            for(int i = 1; i <= num/2; i++){
        if(num%i == 0) answer += i;
      }
        return answer+num;
    }
```



<bold> source: https://programmers.co.kr/learn/courses/30/lessons/12928?language=java </bold>
