TENK_PROMPT = """
Extract:
- Business model
- Revenue drivers
- Margins
- Competitive positioning
- Key risks
"""

TRANSCRIPT_PROMPT = """
Extract:
- What changed vs last quarter
- Management tone
- Guidance changes
- Analyst concerns
"""

BEHAVIOR_PROMPT = """
Identify:
- Vague statements
- Evasive answers
- Over-optimism
"""

HEDGE_FUND_PROMPT = """
What would make a hedge fund take action on this name?
What is mispriced?
"""

FINAL_PROMPT = """
Create memo:

1. Business Snapshot
2. Drivers
3. What Changed
4. Risks (new vs gone)
5. Management Behavior
6. Hedge Fund Signals
7. Bull Case
8. Bear Case
9. KPIs
10. One-line Take
"""
