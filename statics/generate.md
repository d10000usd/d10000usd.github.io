### 파일명을 기반으로 디버깅·테스트 파일을 효율적으로 관리하는 가이드

#### 1. 기본 원칙
| 항목 | 권장 방식 | 이유 |
|------|-----------|------|
| **주 파일명 (`filename`)** | 시스템·모듈을 가장 잘 나타내는 **단일** 영문/한글 조합 (예: `authService`, `paymentProcessor`) | 가독성 ↑, 자동화 스크립트에서 파싱하기 쉬움 |
| **디버깅 파일** | `filename.debug.<ext>` (예: `authService.debug.log`) | 원본 파일과 구분이 명확하고, 파일 종류(`log`, `dump`)를 바로 알 수 있음 |
| **테스트 파일** | `filename.test.<ext>` (예: `authService.test.js`) | 테스트 코드·데이터와 본 코드가 동일한 네이밍 규칙을 공유해 찾기 쉬움 |
| **버전/빌드 구분** | `filename.<버전>.<ext>` 혹은 `filename.<buildID>.<ext>` | CI/CD 파이프라인에서 특정 버전을 바로 매핑 가능 |

#### 2. 파일명 구성 요소
```
<주파일명>.<구분자>.<추가정보>.<확장자>
```
| 구분자 | 사용 예시 | 설명 |
|--------|-----------|------|
| `.` (dot) | `authService.debug.log` | 가장 일반적인 구분자, 다중 레벨 구분 가능 |
| `-` (dash) | `authService-debug.log` | 파일 시스템에 따라 dot이 제한적인 경우 활용 |
| `_` (underscore) | `authService_debug.log` | 가독성 유지와 스크립트 파싱에 용이 |

> **Tip**: 프로젝트 전체에 일관된 구분자를 선택하고, `.editorconfig` 혹은 `prettier` 플러그인으로 강제하면 팀 차원의 혼란을 최소화할 수 있습니다.

#### 3. 디버깅 파일 활용 패턴
1. **실시간 로그**  
   - 파일명: `filename.debug.log`  
   - 로그 레벨(`INFO`, `WARN`, `ERROR`)을 파일 내에 태그하거나, `filename.debug.error.log` 등으로 세분화 가능.

2. **스냅샷·덤프**  
   - 파일명: `filename.debug.dump` 혹은 `filename.debug.core`  
   - 메모리 덤프, CPU 프로파일링 결과를 저장할 때 사용.

3. **자동 회전(Rotation)**  
   - `filename.debug.YYYYMMDD.log` 형태로 날짜를 포함시키면 **logrotate**와 같은 도구와 연동이 쉽습니다.

#### 4. 테스트 파일 활용 패턴
| 테스트 유형 | 파일명 예시 | 비고 |
|------------|------------|------|
| **단위 테스트** | `filename.test.unit.js` | `unit`/`integration` 구분을 추가하면 테스트 스위트 필터링이 용이 |
| **통합 테스트** | `filename.test.int.js` | |
| **시나리오/엔드‑투‑엔드** | `filename.test.e2e.ts` | |
| **데이터/샘플** | `filename.test.data.json` | 테스트용 fixtures를 명시적으로 구분 |

#### 5. CI / CD 파이프라인 연계
```yaml
# 예시: GitHub Actions
steps:
  - name: Run unit tests
    run: |
      npm test -- --testPathPattern=**/${{ env.FILENAME }}.test.unit.js
  - name: Upload debug logs (if failed)
    if: failure()
    uses: actions/upload-artifact@v3
    with:
      name: debug-logs
      path: ${{ env.FILENAME }}.debug.log
```
- **환경 변수(`FILENAME`)**에 주 파일명을 저장해두면, 동일 스크립트가 여러 모듈에 재사용 가능.
- 테스트 결과에 따라 자동으로 해당 `debug` 파일을 아티팩트로 업로드하면, 문제 해결 속도가 크게 향상됩니다.

#### 6. 팀 협업 시 체크리스트
- [ ] `filename` 정의 문서(`README` 혹은 `CONTRIBUTING.md`)에 명시했는가?
- [ ] 디버깅·테스트 파일명 규칙을 **Lint** 규칙으로 자동 검증하고 있는가?
- [ ] 로그·덤프 파일은 **보안**(민감 정보 마스킹) 및 **용량 관리**(자동 압축/삭제) 정책이 적용되는가?
- [ ] 테스트 파일은 CI에서 **병렬 실행**이 가능하도록 독립성을 보장하고 있는가?

#### 7. 실전 예시

```plaintext
src/
├─ authService/
│  ├─ authService.js                ← 메인 구현
│  ├─ authService.debug.log        ← 실행 중 실시간 로그
│  ├─ authService.debug.dump       ← 메모리 덤프
│  ├─ authService.test.unit.js     ← 단위 테스트
│  └─ authService.test.data.json   ← 테스트용 샘플 데이터
├─ paymentProcessor/
│  ├─ paymentProcessor.ts
│  ├─ paymentProcessor.debug.log
│  ├─ paymentProcessor.test.int.ts
│  └─ paymentProcessor.test.data.json
```

- 파일 트리만 보아도 **어디서 어떤 용도로** 파일이 사용되는지 한눈에 파악 가능.
- 스크립트(`npm run debug:auth`)와 CI 파이프라인이 동일한 네이밍 규칙을 활용하므로 **유지보수 비용**이 크게 감소합니다.

---

### 요약
- **`filename`**을 **모듈·시스템 식별자**로 고정하고, **`.debug.`**, **`.test.`** 구분자를 붙여 각각 디버깅·테스트 파일을 명명한다.
- 구분자와 확장자를 일관되게 정하고, CI/CD와 Lint 도구에 적용해 자동화한다.
- 날짜·버전·빌드 ID와 같은 추가 정보를 파일명에 포함시켜 로그 회전·아티팩트 관리가 용이하도록 설계한다.

위 원칙을 프로젝트에 적용하면 파일 탐색, 자동화, 팀 협업 모두에서 **명확성**과 **효율성**을 크게 향상시킬 수 있습니다. 필요에 따라 구체적인 스크립트 예시나 Lint 규칙을 추가로 제공해드릴 수 있으니, 언제든 알려 주세요!