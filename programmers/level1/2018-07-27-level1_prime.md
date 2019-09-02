## 문제: 소수 찾기 

1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

예를 들어, n 이 10이면 [2,3,5,7] 이 소수이니 4를 리턴합니다.


## Java

### My Solution 
```java
class Solution {
  public int solution(int n) {
      int answer = 0;
      boolean isPrime[]=new boolean[n+1];
      
       for (int i = 2; i <= n; i++) 
            isPrime[i] = true;
      
      for(int i=2; i*i<=n; i++){
          if(isPrime[i]){
              for(int j=i;i*j<=n;j++)
                  isPrime[i*j]=false;
          }
      }
      
       for (int i = 2; i <= n; i++) 
            if (isPrime[i]) answer++;
      
      return answer;
  }
    

}
```

### Best solution 
```java

 int numberOfPrime(int n) {
        int result = 0;
        for(int i=2; i<=n; i++){
        for(int j=2; j<=i; j++){
        if(j == i){
            ++result;
        } else if(i%j == 0){
            break;
        }
      }
    }

        return result;
    }

```



<bold> source: https://programmers.co.kr/learn/courses/30/lessons/12921?language=java </bold>
