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

보호소에 들어온 동물들의 아이디와 이름을 ANIMAL_ID순으로 정렬해서 조회하는 쿼리를 해야 한다.

예시)

| ANIMAL_ID  | NAME         |
|------------|--------------|
| A355753	 |	Sugar	    |  
| A382192    |	Jewel   	|  
      

## 해설

일단, ANIMAL_INS의 ANIMAL_ID, NAME이 나와야 한다. 
```SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ```  
그 다음에는 ANIMAL_ID로 정렬해야 한다g
```ORDER BY ANIMAL_ID```   

## Answer

```SQL
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID
```


<bold> source: https://programmers.co.kr/learn/courses/30/lessons/59403?language=mysql </bold>
