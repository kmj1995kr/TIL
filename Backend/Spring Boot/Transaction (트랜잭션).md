지금 개발중인 프로젝트의 개발 표준으로 `service` class에는 `@Transactional` annotation을 사용하도록 권고 되고 있어 해당 문법을 제대로 모른채 사용하고 있었다.

최근 실제로 `@Transational`의 속성을 사용하여 트랜잭션을 관리해야 하는 사례가 생기면서 사용법에 대해 정확히 익히고 알아보는 계기가 되었다!
### Transaction이 뭔데?
> In programming, we refer to a transaction as **a group of related actions that need to be performed as a single action**. In other words, a transaction is a logical unit of work whose effect is visible outside the transaction either in its entirety or not at all. We require this to ensure data integrity in our applications.
> (출처: https://www.baeldung.com/cs/transactions-intro)

프로그래밍에서 트랜젝션이란, **하나의 단위로 묶어져 실행되어야 할 연관된 액션들의 집합**을 말한다.
다른말로, 트랜젝션은 전체가 성공할때는 같이 성공하고, 실패할때는 전체가 같이 실패해야하는 논리적인 업무의 묶음이다. 데이터 무결성을 위해 Transaction에 대한 설정이 반드시 필요하다
### Transaction 설정법
