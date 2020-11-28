## Identity and Access Management (Security)

#### 접근 통제의 요소 (3 Components in Access Control)

**식별 (Identification)**

- Identification and authentication usually happens at the same time
- Identification ex.: User ID

**인증 (Authentication)**

From weakest to strongest...

- Type 1 (Knowledge based): password
- Type 2 (Ownership based): OTP number
- Type 3 (Characteristics based): fingerprints, face ID

**인가 (Authorization)**

**Multi factor authorization (MFA)**: using a combination of different authentication methods to authorize the user (ex. using password and fingerprints)

- **Two factor authorization**: commonly used by online services -- ex. loggin into apple website (need a password and a key sent to your cellphone)

**대칭키**

- 암호화 키와 복호화 키가 동일

- 비밀키, 유일키, 관용 암호화 방식



비대칭키

- 암호화키와 복호화 키가 상이
- 개인키, 공개키 쌍으로 구성
- 공개키 암호화 방식



Policies (Serverless Architecture pg.83)

Identity-based policies

Resource-based policies

**Managed policy**: can be easily reused and be applied to groups

- Easier version control and rollback

**Inline policy**

