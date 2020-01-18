## 문제: 이름이 el로 끝나는 동물 찾기
: WHERE, LIKE 사용하기

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

### Table 

| NAME             | TYPE       | NULLABLE |
|------------------|------------|----------|
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |



### Direction

보호소에 들어온 동물들을 이름과 보호 시작일 순으로 조회해야 한다. 이름이 같다면 나중에 보호를 시작한 동물을 먼저 보여줘야 한

예시)

| NAME         |
|--------------|
|	Jack	   | 
      

## 해설

일단, ANIMAL_INS의  NAME이 나와야 한다. 
```SELECT NAME FROM ANIMAL_INS  ```  
그 다음에는 DATETIME으로 정렬하고 맨 위의 element만 가지고 온다
```ORDER BY DATETIME LIMIT 1```   

## Answer

```SQL
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1
```


<bold> source: https://programmers.co.kr/learn/courses/30/lessons/59405?language=mysql</bold>
