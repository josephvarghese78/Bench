import random
import time
import AccessTokenTest as a
import requests
from datetime import datetime
import time
import config as cfg
import json
import uuid
from decorators import task
from requests.models import Response

token="eyJ0eXAiOiJKV1QiLCJub25jZSI6IkVsMS1adFNLaUpwb3JWV3FLUDROZ2N0RDZtbnI4T2prVWpmd0xzRGo5MkkiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC81ZDNlMjc3My1lMDdmLTQ0MzItYTYzMC0xYTBmNjhhMjhhMDUvIiwiaWF0IjoxNzc0NDAzNzI5LCJuYmYiOjE3NzQ0MDM3MjksImV4cCI6MTc3NDQwODk4NCwiYWNjdCI6MCwiYWNyIjoiMSIsImFjcnMiOlsicDEiXSwiYWlvIjoiQVhRQWkvOGJBQUFBNGFhOVpFN0w0OXdTSGROdUlmSHZKUVU0NTU5TFZ3ZzFLa1J2cjF1Z0dsQ3lUZTlZTDVmckRpK3lrTDlUQjh4MkZidVE1R2ZGZ2drTHd6ZmlnZmg2UWxrUzV5Um9yNG1peXl5TjcxWFlac0Nzb0daRXVSRCtEeFY3WDFzbkh1MHIxSWJnazB2UndBSlFZelhSUk02bXpRPT0iLCJhbXIiOlsicHdkIiwicnNhIiwibWZhIl0sImFwcF9kaXNwbGF5bmFtZSI6ImdmX2Fza2hyX2FpX3Byb2QiLCJhcHBpZCI6ImRkODY1MzZlLTRmZGMtNDRhMi04YzAyLWMwNWU2YmRmZTZmMSIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiOWU2OWRlODktZTJjYi00ZWJlLWI4NjMtOGY4NmZiMDQ1Njk3IiwiZmFtaWx5X25hbWUiOiJWYXJnaGVzZSIsImdpdmVuX25hbWUiOiJKb3NlcGgiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxMzYuMjI2Ljc3LjEwMyIsIm5hbWUiOiJKb3NlcGggVmFyZ2hlc2UiLCJvaWQiOiJkYWM4MGJlNS02NzQxLTRjZjYtODViYS03ZDY5MjE2YTUyMzEiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtNDA3MjIwNDUwOS0xOTg1MDQzMDY2LTExMDY5NDUxODktNjQxMTEyIiwicGxhdGYiOiI1IiwicHVpZCI6IjEwMDMyMDAwOUI1MURGRjMiLCJyaCI6IjEuQVJNQWN5Yy1YWF9nTWtTbU1Cb1BhS0tLQlFNQUFBQUFBQUFBd0FBQUFBQUFBQUFUQVBvVEFBLiIsInNjcCI6IlVzZXIuUmVhZCBwcm9maWxlIG9wZW5pZCBlbWFpbCIsInNpZCI6IjAwMzE3ODJhLTQyNDItYzAxNC0xZjQ0LTQyOTAzYWUwZTFmNSIsInNpZ25pbl9zdGF0ZSI6WyJkdmNfbW5nZCIsImR2Y19jbXAiLCJpbmtub3dubnR3ayIsImttc2kiXSwic3ViIjoiUkFHU3g5VzFGS0V4YU1xUVctdngtX2FYMXRJbmQ4UndMa1RwMWhSX2NlVSIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJOQSIsInRpZCI6IjVkM2UyNzczLWUwN2YtNDQzMi1hNjMwLTFhMGY2OGEyOGEwNSIsInVuaXF1ZV9uYW1lIjoidmFyZ2hqb0BNRkNHRC5DT00iLCJ1cG4iOiJ2YXJnaGpvQE1GQ0dELkNPTSIsInV0aSI6ImlVRGlla2tTX0VHMHdfblBaWUpTQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfYWNkIjoxNzcwMTI4ODY4LCJ4bXNfYWN0X2ZjdCI6IjMgOSIsInhtc19mdGQiOiJBSV9nV2lQU1RJNXFSWU9PbGx6UGRhOWdlSko2NzFJRUlJR1lDdWtGU1JZQmRYTnpiM1YwYUMxa2MyMXoiLCJ4bXNfaWRyZWwiOiIxIDIiLCJ4bXNfcGZ0ZXhwIjoxNzc0NDk1Mzg0LCJ4bXNfc3QiOnsic3ViIjoidVpELUVKYmtKSXZIQXpianVVV0ZzY0l3c1FsQzBDS3VUMFRvT0hGMkNSTSJ9LCJ4bXNfc3ViX2ZjdCI6IjMgMiIsInhtc190Y2R0IjoxMzk5OTk0ODkzLCJ4bXNfdG50X2ZjdCI6IjMgMTAifQ.bGfjy04Xcv3V6pS7vVjfD9h20_vExYtjx2TbkdhVO7bowAhfwx2VX94GUvitygzZPgQgF52HSqW9im-imHUyBfvH5TAr60JcGYohuIhESdbt7XRf_HVgBOK84j6p6YyhS3Hk0bPBEpEz-_hbCia1VfAfL-JxDCZR0CGjn8Vbh-2SoXQu2LyL817P5hxMTEB9aiUBXXGOOF08VBqm1_R8H_rb_QnLTuT2KK0lsibET23Uo3rkZTf4FznYMmo_XeSJ7P72Dk-2s7PJibqjr5Hrp_gAiuAZijtjuIJSHJENyYPWLofEu56SH8PhDOv8KH6owwX9tUWanEsvdDUY9GpkFQ"
CHAT_QUESTIONS = [
    "what are Canada vacation policies?",
    "can i use vacation time to take courses?",
    "how do i get tuition reimbursement?",
    "what is the parental leave policy?",
    "how do i reset my password?",
]
MULTILINGUAL_QUESTIONS = [
    ("en", "what are Canada vacation policies?"),
    ("fr", "Quelles ressources sont disponibles pour l'intégration des nouveaux arrivants?"),
    ("zh", "我在哪里可以查看工资单？"),
    ("zht", "新員工入職有哪些資源可用？"),
    ("ja", "年次休暇残高を確認するにはどうすればよいですか？"),
    ("vi", "Làm thế nào để kiểm tra số dư nghỉ phép hàng năm của tôi?"),
    ("pt", "quais são as políticas de férias no Canadá?"),
    ("es", "¿cuáles son las políticas de vacaciones en Canadá?"),
    ("id", "Bagaimana cara memeriksa saldo cuti tahunan saya?")
]

CHAT_QUESTIONS_MXD = [
    "Why isn’t my vacation balance in Workday showing the right number of days?",
    "When do I start earning an extra vacation day?",
    "As a leader, I need a comprehensive, step‑by‑step view to resolve multiple items that span Time Off, Pay & Tax, Recruiting, and day‑to‑day Workday maintenance. My vacation balance is off after a carryover, and I need to know when an extra day is earned, the exact rules for cash in lieu, and how sick and personal days are handled when a business event overlaps with a public holiday. One direct report is starting maternity leave while another is on disability leave; I require a manager‑action checklist for initiating, approving, and monitoring both leaves, including how to support a gradual return, document performance during that period, and determine overtime eligibility and time‑in‑lieu coding. On payroll, I need to retrieve payslips, confirm availability of T4 and potentially a T2200 for a remote employee, understand a temporary spike in taxes, and verify whether backpay or rate changes triggered extra deductions. I also need to open or backfill a requisition, confirm approvals, check requisition status, review applications, ensure referral handling is correct, and validate that onboarding tasks and delegation settings are in place for a new hire, including mass‑move scenarios and remote/hybrid updates. Finally, I’d like to review the last performance ratings, goal updates, and recognition options, and know the correct process for exits in Workday should the need arise",
    "Can I carry over my unused Personal or sick days?",
    "Can I get cash in lieu of using all my vacation days?",
    "My direct report is going on a Maternity leave, what do I need to do?",
    "My direct report needs to go on disability leave, what do I need to do / how can I support them?",
    "I’m a people leader working primarily in Workday and AskHR, and I’m trying to reconcile a handful of operational items that cross Vacation, Time Off, Pay & Tax, and Recruiting. My vacation balance in Workday doesn’t appear to match what I expect after a recent carryover and a business event; I also need clarity on when an extra vacation day accrues and whether cash in lieu is available. One direct report is moving from maternity leave into a gradual return, and I’d like to confirm which steps and approvals I’m responsible for, what documentation is needed, and whether overtime eligibility changes during that transition. Separately, I need to locate payslips and the latest tax slips (T4, T2200 if applicable), validate why taxes spiked on a recent pay, and confirm whether backpay will trigger additional deductions. Finally, I want to check the status of a backfill requisition and ensure my new hire’s onboarding tasks are visible",
    "Is my direct report eligible for overtime?",
    "Why are my taxes so much higher on this pay?",
    "Where can I find / download my payslip?",
    "How do I find the last performance review for my direct report?",
    "When was the last time my direct report had a promotion?",
    "I manage a distributed team and I’m seeing several issues across AskHR and Workday that I need to resolve in one go. First, my Workday vacation balance doesn’t reflect carryover correctly after a performance package increase, and I’m unsure how personal days, sick days, blackout periods, and cash in lieu intersect with maternity leave, a declared holiday, and a gradual return schedule. Second, I have to guide a direct report through disability leave and then a phased return; I need a clear checklist for manager actions, approvals, and any changes to overtime eligibility, along with how to record time in lieu. Third, on payroll: I need recent and historical payslips, an explanation of why taxes jumped on the last cycle, and whether benefits or garnishments affected net pay. Lastly, I need to backfill a role: what’s the correct job requisition path, how do I confirm approvals, and where do I track applications and onboarding readiness for the new hire?",
    "What is my direct report’s performance rating?",
    "How do I update my goals in Workday?",
    "How do I update my skills / work experience / education (Career Profile) in Workday?",
    "How do I find out about internal job postings?",
    "How do I find / apply to an internal job posting?",
    "How can I refer a friend to a job at Manulife?",
    "I need to backfill a role on my team, how do I get started?",
    "I’m a manager supporting a team across multiple regions, and I’m trying to resolve several related issues in Workday and AskHR. My vacation balance doesn’t appear to be updating correctly after carryover, and I need to understand how personal days, sick days, and time in lieu should be handled when there is a public holiday or a blackout period. One of my direct reports is preparing for maternity leave, and I want to ensure I complete all required manager actions, approvals, and documentation, including how overtime eligibility is affected. I also need help accessing payslips, understanding why taxes increased on a recent pay, and confirming when T4 forms become available in Workday. Additionally, I’m backfilling a role and would like to know how to track requisition approvals, referrals, and onboarding progress for the new hire",
    "What’s the status of my requisition?",
    "How many applications have I gotten to my job posting?",
    "Why don’t I see my new hire yet in Workday?",
    "What onboarding support is available for my new hire?",
    "How do I handle a performance concern on my team?",
    "How do I add a course I did outside of Manulife to my learning transcript?",
    "As a people leader, I need guidance on several interconnected topics spanning Time Off, Pay & Tax, and Recruiting. My Workday vacation balance changed unexpectedly, and I’m unsure whether this is due to years of service, carryover limits, or a performance-related vacation increase. I also need clarity on whether unused vacation can be paid out as cash in lieu and how this interacts with sick leave and personal days. One employee on my team is transitioning from disability leave into a gradual return, and I want to confirm my responsibilities around approvals, overtime eligibility, and time‑in‑lieu coding. On the payroll side, I need to retrieve historical payslips, understand a spike in income tax deductions, and verify whether backpay or benefit deductions impacted net pay. Finally, I need support creating and approving a job requisition, reviewing applications, and ensuring onboarding tasks are visible for a new hire",
    "How can I recognize my team for going above and beyond on a project?",
    "What option should I select when terminating a direct report in Workday?",
    "How do I mass move a bunch of workers from one leader to another?",
    "How do I change a direct report from hybrid to remote?",
    "I’m responsible for managing several employee lifecycle activities and need a consolidated explanation of how to handle them correctly in AskHR and Workday. My vacation balance appears incorrect after carryover, and I need to understand how vacation entitlement increases with years of service, how personal and sick days are treated, and what happens when leave overlaps with a public holiday or a business event. One direct report is starting maternity leave while another is on disability leave, and I need a clear manager checklist covering required actions, approvals, documentation, and how overtime eligibility or performance tracking is handled during leave and gradual return. In addition, I’m seeing unexpected deductions on payroll and need to access payslips, understand tax calculations, confirm when T4s are issued, and determine whether backpay caused additional deductions. I’m also working on backfilling a role, tracking requisition approvals, managing referrals, and ensuring onboarding, delegation, and team structure updates are completed correctly",
    "Can my EA manage my Workday inbox for me?",
    "Could you please provide me the pay slip from Oct 2019 to Dec 2019",
    "Provide a copy of my first pay slips for May 2018 to July 31, 2018",
    "How can I access my payslip from home?",
    "How can an employee on leave access their T4 without Workday?",
    "Can I get a T2200 tax form as a full time remote employee?",
    "Will I receive tax slips for severance paid in 2024?",
    "When are T4s available in Workday?",
    "As a leader, I’m looking for a detailed, end‑to‑end explanation to resolve multiple employee and manager issues that span Time Off, Pay & Tax, Recruiting, and ongoing Workday maintenance. My vacation balance changed after carryover, and I need to know how many days can be carried forward, when an extra vacation day is earned, and how cash in lieu works, especially if leave overlaps with a public holiday or blackout period. I’m supporting one direct report going on maternity leave and another transitioning from disability leave into a gradual return, and I want a clear checklist of manager responsibilities, approvals, documentation, overtime eligibility, and time‑in‑lieu coding. On payroll, I need to retrieve current and historical payslips, understand why income tax and benefit deductions increased on a recent pay, confirm availability of T4 and T2200 forms, and determine whether backpay or pay‑rate changes triggered adjustments. I’m also opening and backfilling job requisitions, tracking approvals, reviewing applications, managing referrals, ensuring onboarding tasks are completed, updating delegation and reporting relationships, and understanding the correct process for performance reviews, recognition, and potential exits in Workday.",
    "T4 generates blank page when printing",
    "Missed gradual return hours after payroll cutoff – can hours be included next cycle?",
    "I am a new hire and didn’t receive my paycheck",
    "How much will be deducted from my backpay for used vacation and sick leave?",
    "Should maternity pay be deducted from separation pay?",
    "My increased pay rate is not reflected in my paycheck",
    "Unexpected Income Tax / Non-permanent deduction",
    "Annual contract pay does not match monthly payment",
    "Benefits deduction taken bi-weekly instead of monthly",
    "How many pays will be garnished to repay Manulife?",
    "How is my federal tax calculated?",
    "Who can I refer for a job at Manulife?",
    "Can I hire someone in another country?",
    "I’m trying to resolve several issues that affect both my team and my own employee records in Workday and AskHR. My vacation balance does not reflect what I expected after carryover, and I need guidance on how sick days, personal days, and time in lieu are applied, particularly when a public holiday or business event is involved. One of my direct reports is preparing for a leave of absence, and I want to understand my role as a manager, including approvals, documentation, overtime eligibility, and how to support a gradual return to work. I also need assistance accessing payslips, understanding unexpected tax deductions, confirming when tax slips such as T4s are issued, and verifying whether backpay affected net pay. In parallel, I’m working on recruiting and onboarding, including backfilling a role, tracking requisition status, managing referrals, and ensuring onboarding and delegation tasks are completed correctly.",
    "Where is the leader QA link for short term assignment?",
    "Submitted referral without resume – how to fix?",
    "Am I eligible for referral bonus after 3 months?",
    "Are there interview guides and rating guidelines?",
    "Is tenure required before applying for internal jobs?",
    "Do I need tickets for internal employee transfer across segments?",
    "Cannot find former employee position when backfilling",
    "Leader flag disabled during gradual return – cannot create job req",
    "Status of contingent to permanent requisition",
    "Cannot accept transfer due to no available job req",
    "Requisitions awaiting approval in Workday",
    "Posting replacement before employee departure",
    "What time off am I entitled to after family bereavement?",
    "Why did my annual leave change from 15 to 17 days?",
    "How do I use carry over leave this year?",
    "How to add vacation with existing business event request",
    "Vacation carry over not reflected correctly in Workday",
    "Years of service required for 4 weeks vacation",
    "Can sick day be used for acupuncture or physiotherapy?",
    "Guidance on Time in Lieu code",
    "Blackout leave policy timing",
    "Workday not allowing personal day request",
    "When does contract vacation entitlement start?",
    "Workday and Verint time off mismatch",
    "Error submitting BU holiday leave",
    "Working on public holiday – can leave be taken later?",
    "Error Quantity per Day when submitting sick day",
    "How does vacation cash in lieu work?",
    "How many vacation days can be carried over?",
    "Is day after Thanksgiving a public holiday?",
    "Increasing vacation as part of performance package",
    "15 year anniversary vacation entitlement",
    "Vacation balance after maternity leave",
    "Does filed leave auto-cancel if declared holiday?"
]

MULTILINGUAL_QUESTIONS_MXD = [
        ("en", "Who can I refer for a job at Manulife?"),
        ("en", "Can I hire someone in another country?"),
        ("en", "I’m trying to resolve several issues that affect both my team and my own employee records in Workday and AskHR. My vacation balance does not reflect what I expected after carryover, and I need guidance on how sick days, personal days, and time in lieu are applied, particularly when a public holiday or business event is involved. One of my direct reports is preparing for a leave of absence, and I want to understand my role as a manager, including approvals, documentation, overtime eligibility, and how to support a gradual return to work. I also need assistance accessing payslips, understanding unexpected tax deductions, confirming when tax slips such as T4s are issued, and verifying whether backpay affected net pay. In parallel, I’m working on recruiting and onboarding, including backfilling a role, tracking requisition status, managing referrals, and ensuring onboarding and delegation tasks are completed correctly."),
        ("en", "Where is the leader QA link for short term assignment?"),
        ("en", "Submitted referral without resume – how to fix?"),
        ("en", "Am I eligible for referral bonus after 3 months?"),
        ("en", "Are there interview guides and rating guidelines?"),
        ("en", "Is tenure required before applying for internal jobs?"),
        ("en", "Do I need tickets for internal employee transfer across segments?"),
        ("en", "Cannot find former employee position when backfilling"),
        ("en", "Leader flag disabled during gradual return – cannot create job req"),
        ("fr", "Pourquoi mon solde de vacances dans Workday n’affiche-t-il pas le bon nombre de jours?"),
        ("fr", "Quand est-ce que je commence à gagner un jour de congé supplémentaire?"),
        ("fr", "En tant que leader, j’ai besoin d’une vue complète et étape par étape pour résoudre plusieurs points qui couvrent le temps libre, la paie et les impôts, le recrutement et la maintenance quotidienne de Workday. Mon solde de vacances est décalé après un report, et j’ai besoin de savoir quand une journée supplémentaire est gagnée, les règles exactes pour l’argent en compensation, et comment les journées de maladie et personnelles sont gérées lorsqu’un événement d’affaires chevauche un jour férié. Un subordonné direct commence un congé de maternité tandis qu’un autre est en congé d’invalidité; J’exige une liste de vérification des actions du gestionnaire pour initier, approuver et surveiller les deux congés, y compris comment soutenir un retour graduel, documenter la performance durant cette période, et déterminer l’admissibilité aux heures supplémentaires et le codage du temps en remplacement. Sur la paie, je dois récupérer des talons de paie, confirmer la disponibilité d’un T4 et potentiellement d’un T2200 pour un employé à distance, comprendre une hausse temporaire d’impôts, et vérifier si les rétropaiements ou les changements de taux ont déclenché des déductions supplémentaires. Je dois aussi ouvrir ou renouveler une demande, confirmer les approbations, vérifier le statut de la demande, examiner les demandes, m’assurer que la gestion des références est correcte et valider que les tâches d’intégration et les paramètres de délégation sont en place pour une nouvelle embauche, y compris les scénarios de déménagement massif et les mises à jour à distance/hybride. Enfin, j’aimerais revoir les dernières évaluations de performance, les mises à jour d’objectifs et les options de reconnaissance, et connaître le bon processus pour les sorties dans Workday si besoin s’en fait sentir."),
        ("fr", "Puis-je transférer mes jours personnels ou de maladie non utilisés?"),
        ("fr", "Quelles ressources sont disponibles pour l'intégration des nouveaux arrivants?"),
        ("fr", "Puis-je avoir de l’argent comptant au lieu d’utiliser tous mes jours de vacances?"),
        ("fr", "Je gère une équipe distribuée et je vois plusieurs problèmes chez AskHR et Workday que je dois résoudre d’un coup. Premièrement, mon solde de congé Workday ne reflète pas correctement le report après une augmentation du forfait de performance, et je ne comprends pas comment les journées personnelles, les congés de maladie, les périodes de blackout et l’argent en compensation s’interagissent avec le congé de maternité, un congé déclaré et un calendrier de retour graduel. Deuxièmement, je dois guider un subordonné direct à travers un congé d’invalidité puis un retour progressif; J’ai besoin d’une liste claire pour les actions des gestionnaires, les approbations et tout changement d’admissibilité aux heures supplémentaires, ainsi que pour enregistrer le temps de substitution. Troisièmement, sur la paie : j’ai besoin de fiches de paie récentes et historiques, d’une explication sur les raisons pour lesquelles les impôts ont augmenté lors du dernier cycle, et si les prestations ou saisies sur la rémunération nete ont affecté. Enfin, je dois combler un poste : quel est le bon chemin pour la demande d’emploi, comment puis-je confirmer les approbations, et où suivre les candidatures et la préparation à l’intégration pour la nouvelle embauche?"),
        ("fr", "Comment puis-je trouver la dernière évaluation de performance pour mon subordonné direct?"),
        ("fr", "Comment puis-je mettre à jour mes compétences / expérience professionnelle / formation (profil de carrière) dans Workday?"),
        ("zh", "我的直属下属的绩效评分是多少？"),
        ("zh", "我如何在 Workday 中更新我的目标？"),
        ("zh", "我如何在 Workday 中更新我的技能 / 工作经验 / 教育（职业档案）？"),
        ("zh", "我怎么知道内部招聘信息？"),
        ("zh", "我如何查找 / 申请内部职位发布？"),
        ("zh", "我怎样才能推荐朋友去曼利工作？"),
        ("zh", "我需要在团队中顶替一个角色，我该怎么开始？"),
        ("zh", "我的申请状态如何？"),
        ("zh", "我已经收到多少份申请了？"),
        ("zh", "为什么我还没在 Workday 看到我的新员工？"),
        ("zh", "我的新员工有哪些入职支持？"),
        ("zh", "我该如何处理团队中的绩效问题？"),
        ("zh", "我在哪里可以查看工资单？"),
        ("zht", "我該如何表彰團隊在專案上超越預期的付出？"),
        ("zht", "在 Workday 終止直接下屬時，我應該選擇哪個選項？"),
        ("zht", "我要怎麼把一群工人從一個領導者轉移到另一個領導者？"),
        ("zht", "我該如何將直接下屬從混合工作改為遠端工作？"),
        ("zht", "我負責管理多項員工生命週期活動，需要一個綜合說明，說明如何在 AskHR 和 Workday 中正確處理這些活動。結轉後我的假期餘額似乎不正確，我需要了解假期權益如何隨著服務年資增加而增加，個人假和病假如何被處理，以及當假期與公共假期或商務活動重疊時會發生什麼事。一位直屬下屬即將開始產假，另一位則在休傷病假，我需要一份明確的主管清單，涵蓋所需行動、核准、文件，以及在休假和逐步返工期間如何處理加班資格或績效追蹤。此外，我在薪資上看到意外扣款，需要查看薪資單、了解稅務計算、確認 T4 何時發出，以及判斷補發薪資是否造成額外扣除。我也在補缺職缺、追蹤申請核准、管理推薦，並確保入職、委派和團隊架構更新正確完成。"),
        ("zht", "我的助理助理可以幫我管理我的 Workday 收件匣嗎？"),
        ("zht", "請提供2019年10月至2019年12月的薪資單"),
        ("zht", "請提供我2018年5月至2018年7月31日的第一份薪資單副本"),
        ("zht", "我怎麼能從家裡取得我的薪資單？"),
        ("zht", "請假的員工如何在沒有 Workday 的情況下存取他們的 T4？"),
        ("zht", "我作為全職遠端員工，可以申請 T2200 報稅表嗎？"),
        ("zht", "我會在2024年收到遣散費的稅務單嗎？"),
        ("zht", "T4 何時會在 Workday 上可用？"),
        ("ja", "T4は印刷時に白紙を生成する"),
        ("ja", "給与計算締め切り後の段階的復帰時間を逃した – 次のサイクルに勤務時間を含めることは可能か?"),
        ("ja", "私は新入社員で、給料を受け取っていません"),
        ("ja", "使用済みの休暇と病気休暇の遡及分からいくら差し引かれるのですか?"),
        ("ja", "産休手当は退職手当から差し引かれるべきか?"),
        ("ja", "私の給与増加は給料には反映されていません"),
        ("ja", "予期せぬ所得税 / 非恒久的控除"),
        ("ja", "年間契約給与は月々の支払いに見合っていない"),
        ("ja", "給付金控除は月ごとではなく隔週で行われる"),
        ("ja", "マニュライフへの返済のために、いくつの給与が差し押さえられるのか?"),
        ("ja", "私の連邦税はどのように計算されるのですか?"),
        ("ja", "マニュライフでの仕事は誰を紹介すればいいですか?"),
        ("ja", "年次休暇残高を確認するにはどうすればよいですか？"),
        ("vi", "Làm việc vào ngày nghỉ lễ – có thể nghỉ sau không?"),
        ("vi", "Số lượng lỗi mỗi ngày khi gửi ngày ốm"),
        ("vi", "Tiền mặt thay cho kỳ nghỉ hoạt động như thế nào?"),
        ("vi", "Có thể chuyển bao nhiêu ngày nghỉ?"),
        ("vi", "Ngày sau Lễ Tạ ơn có phải là ngày nghỉ lễ không?"),
        ("vi", "Tăng kỳ nghỉ như một phần của gói hiệu suất"),
        ("vi", "Quyền lợi nghỉ dưỡng kỷ niệm 15 năm"),
        ("vi", "Cân bằng kỳ nghỉ sau khi nghỉ thai sản"),
        ("vi", "Nghỉ phép đã nộp có tự động hủy nếu được tuyên bố là ngày nghỉ không?"),
        ("vi", "Làm thế nào để kiểm tra số dư nghỉ phép hàng năm của tôi?"),
        ("pt", "Não é possível encontrar uma vaga de ex-funcionário durante o backfill"),
        ("pt", "Bandeira de líder desativada durante retorno gradual – não é possível criar requisição de vaga"),
        ("pt", "Status de contingente para requisição permanente"),
        ("pt", "Não posso aceitar uma transferência por falta de vaga disponível"),
        ("pt", "Requisições aguardando aprovação no Workday"),
        ("pt", "Postar substituição antes da saída do funcionário"),
        ("pt", "A que tempo eu tenho direito após o luto familiar?"),
        ("pt", "Por que minhas férias anuais mudaram de 15 para 17 dias?"),
        ("pt", "Como utilizo as férias transferidas neste ano?"),
        ("pt", "Como adicionar férias a uma solicitação existente de evento empresarial"),
        ("pt", "Transferência de férias não refletida corretamente no Workday"),
        ("pt", "Anos de serviço necessários para 4 semanas de férias"),
        ("pt", "O dia de doença pode ser usado para acupuntura ou fisioterapia?"),
        ("pt", "Quais são as políticas de férias no Canadá?"),
        ("es", "¿cuáles son las políticas de vacaciones en Canadá?"),
        ("id", "Saya karyawan baru dan tidak menerima gaji saya"),
        ("id", "Berapa banyak yang akan dipotong dari gaji saya untuk liburan dan cuti sakit bekas?"),
        ("id", "Haruskah gaji bersalin dipotong dari gaji pemisahan?"),
        ("id", "Kenaikan gaji saya tidak tercermin dalam gaji saya"),
        ("id", "Pajak Penghasilan Tidak Terduga / Pengurangan Tidak Tetap"),
        ("id", "Gaji kontrak tahunan tidak sesuai dengan pembayaran bulanan"),
        ("id", "Pengurangan tunjangan diambil dua mingguan, bukan bulanan"),
        ("id", "Berapa banyak gaji yang akan dihiasi untuk membayar kembali Manulife?"),
        ("id", "Bagaimana pajak federal saya dihitung?"),
        ("id", "Siapa yang dapat saya referensikan untuk pekerjaan di Manulife?"),
        ("id", "Bisakah saya mempekerjakan seseorang di negara lain?"),
        ("id", "Bagaimana cara memeriksa saldo cuti tahunan saya?")
]

def classify_complexity(question: str) -> str:
    length = len(question)

    if length <= 50:
        return "low"
    elif 50 < length <= 500:
        return "medium"
    else:
        return "high"


@task(name='askhr-en-chat', weight=4)
def en_chat(user_session):
    previous_interactions = False
    prev_int = ""
    url = "https://cacp-gaa-gfthr-be-app.azurewebsites.net/v1/query"
    question=random.choice(CHAT_QUESTIONS)

    payload={
      "userid": "dac80be5-6741-4cf6-85ba-7d69216a5231",
      "ssid": "cef59a3b-167b-4127-9c91-d1028aaa7062",
      "country": "CAN",
      "department": "GDO-NON PROJECT",
      "segment": "Corporate & Other",
      "employeeTitle": "Director, Lead Quality Engineer",
      "employeeType": "Y",
      "employeeId": "421324",
      "officeLocation": "CAN, Ontario, Toronto, 200 Bloor Street East",
      "username": "Joseph Varghese",
      "email": "Joseph_Varghese@manulife.com",
      "userPrincipalName": "varghjo@MFCGD.COM",
      "current_query": question,
      "previous_interactions": "",
      "signature": [],
      "language": "en",
      "access_token": token
    }

    resp = user_session.post(url=url, json=payload)
    if previous_interactions:
        ai_response = resp.json().get("response", "")
        if len(ai_response) > 0:
            prev_int += "::::" if len(prev_int) > 0 else ""
            prev_int += f"{question}::::{ai_response}"

    return resp, en_chat.test_name


@task(name='askhr-ml-chat', weight=2)
def ml_chat(user_session):
    previous_interactions=False
    prev_int = ""
    url = "https://cacp-gaa-gfthr-be-app.azurewebsites.net/v1/query"
    locale, question =random.choice(MULTILINGUAL_QUESTIONS)

    payload={
      "userid": "dac80be5-6741-4cf6-85ba-7d69216a5231",
      "ssid": "cef59a3b-167b-4127-9c91-d1028aaa7062",
      "country": "CAN",
      "department": "GDO-NON PROJECT",
      "segment": "Corporate & Other",
      "employeeTitle": "Director, Lead Quality Engineer",
      "employeeType": "Y",
      "employeeId": "421324",
      "officeLocation": "CAN, Ontario, Toronto, 200 Bloor Street East",
      "username": "Joseph Varghese",
      "email": "Joseph_Varghese@manulife.com",
      "userPrincipalName": "varghjo@MFCGD.COM",
      "current_query": question,
      "previous_interactions": "",
      "signature": [],
      "language": locale,
      "access_token": token
    }

    resp = user_session.post(url=url, json=payload)
    if previous_interactions:
        ai_response = resp.json().get("response", "")
        if len(ai_response) > 0:
            prev_int += "::::" if len(prev_int) > 0 else ""
            prev_int += f"{question}::::{ai_response}"

    return resp,  ml_chat.test_name


@task(name='askhr-en-chat-mxd', weight=4, enabled=False)
def en_chat_mxd(user_session):
    previous_interactions = False
    prev_int = ""
    url = "https://cacp-gaa-gfthr-be-app.azurewebsites.net/v1/query"
    question=random.choice(CHAT_QUESTIONS_MXD)

    payload={
      "userid": "dac80be5-6741-4cf6-85ba-7d69216a5231",
      "ssid": "cef59a3b-167b-4127-9c91-d1028aaa7062",
      "country": "CAN",
      "department": "GDO-NON PROJECT",
      "segment": "Corporate & Other",
      "employeeTitle": "Director, Lead Quality Engineer",
      "employeeType": "Y",
      "employeeId": "421324",
      "officeLocation": "CAN, Ontario, Toronto, 200 Bloor Street East",
      "username": "Joseph Varghese",
      "email": "Joseph_Varghese@manulife.com",
      "userPrincipalName": "varghjo@MFCGD.COM",
      "current_query": question,
      "previous_interactions": "",
      "signature": [],
      "language": "en",
      "access_token": token
    }

    resp = user_session.post(url=url, json=payload)
    if previous_interactions:
        ai_response = resp.json().get("response", "")
        if len(ai_response) > 0:
            prev_int += "::::" if len(prev_int) > 0 else ""
            prev_int += f"{question}::::{ai_response}"

    return resp, f"{en_chat_mxd.test_name}_{classify_complexity(question)}"


@task(name='askhr-ml-chat-mxd', weight=2, enabled=False)
def ml_chat_mxd(user_session):
    previous_interactions=False
    prev_int = ""
    url = "https://cacp-gaa-gfthr-be-app.azurewebsites.net/v1/query"
    locale, question =random.choice(MULTILINGUAL_QUESTIONS_MXD)

    payload={
      "userid": "dac80be5-6741-4cf6-85ba-7d69216a5231",
      "ssid": "cef59a3b-167b-4127-9c91-d1028aaa7062",
      "country": "CAN",
      "department": "GDO-NON PROJECT",
      "segment": "Corporate & Other",
      "employeeTitle": "Director, Lead Quality Engineer",
      "employeeType": "Y",
      "employeeId": "421324",
      "officeLocation": "CAN, Ontario, Toronto, 200 Bloor Street East",
      "username": "Joseph Varghese",
      "email": "Joseph_Varghese@manulife.com",
      "userPrincipalName": "varghjo@MFCGD.COM",
      "current_query": question,
      "previous_interactions": "",
      "signature": [],
      "language": locale,
      "access_token": token
    }

    resp = user_session.post(url=url, json=payload)
    if previous_interactions:
        ai_response = resp.json().get("response", "")
        if len(ai_response) > 0:
            prev_int += "::::" if len(prev_int) > 0 else ""
            prev_int += f"{question}::::{ai_response}"

    return resp,  f"{ml_chat_mxd.test_name}_{classify_complexity(question)}"