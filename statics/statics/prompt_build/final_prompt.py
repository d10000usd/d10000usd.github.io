final_prompt=""

final_prompt = self._prompt_service.build_final_prompt(
    session_id=session_id,
    user_question=(user_req.ask or "").replace("", "")
)
if user_req.ask and ('킵' in user_req.ask and '리본' in user_req.ask or '' in user_req.ask):
    # 도구목록 키워드 확인 및 도구 정보 추가
    final_prompt = await self._prompt_service.enhance_prompt_with_tools(
        prompt=final_prompt,
        user_question=(user_req.ask or ""),
        session_id=session_id
    )