# SQL 이란?

**SQL(Structured Query Language)**란 **관계형 데이터베이스 시스템(RDBMS)**에서 데이터를 관리하기 위해 만들어진 특수 목적의 프로그래밍 언어이다. (위키백과)

- **DBMS (Database Management System)**를 통해 데이터를 조작하고 관리할 수 있다
  - SQL계의 IDE와 같은 느낌!
  - 각각의 소프트웨어 마다 조금식 다른 문법과 기능을 지원한다
  - **Oracle (PL/SQL)**: 기업단위로 주로 사용하는 DBMS, 오픈소스로 운영되지 않는다
  - **MySQL**: 오픈소스로 운영되며, 중소기업이나 개인용도로도 많이 쓰인다
  - 그 외 SQLite, PostgreSQL, MariaDB, SQL Server등 다양한 DBMS가 존재한다

### SQL / 관계형 데이터베이스의 특징

1. Column과 Row를 가진 2차원 Table 형태로 이루어져있다 
   1. Column: 테이블에서 한 속성을 의미하며, field라고도 불린다
   2. Row: 데이터 한 줄을 의미하며, record라고도 불린다
      

<img src="https://user-images.githubusercontent.com/7082025/58648343-57cd9a00-82be-11e9-87a2-146b4803e482.png"> 



### SQL 문장의 종류 (DML, DDL, DCL, TCL)

| 종류                  | 명령어                         |
| --------------------- | ------------------------------ |
| 데이터 조작어 (DML)   | SELECT, INSERT, UPDATE, DELETE |
| 데이터 정의어 (DDL)   | CREATE, ALTER, DROP, RENAME    |
| 데이터 제어어 (DCL)   | GRANT, REVOKE                  |
| 트랜젝션 제어어 (TCL) | COMMIT, ROLLBACK               |

