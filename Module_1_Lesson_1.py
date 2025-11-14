"""
Module 1 - Lesson 1
MPP (Mentor-Protégé Program) Learning Module

Generated from: MPP Objectives Learning spreadsheet
File Search Store: fileSearchStores/mppsopdocumentation-j83n2w5zjn96
"""

from google import genai
from google.genai import types
import os

# Configuration
GOOGLE_API_KEY = 'AIzaSyCojqFfCCPTalhem7ceRLrr6hfNpqPhaNk'
FILE_SEARCH_STORE = 'fileSearchStores/mppsopdocumentation-j83n2w5zjn96'

# Initialize client
client = genai.Client(api_key=GOOGLE_API_KEY)

# Learning Objectives
LEARNING_OBJECTIVES = [
    "Trace the MPP from its FY1991 pilot origins to its current permanent authority under 10 U.S.C. § 4902.",
    "Identify the legal authority (10 U.S.C. § 4902) and implementing regulation (DFARS Appendix I) for the MPP.",
    "Explain the purpose of approved developmental assistance and how MPAs are structured to enhance Protégé capabilities.",
    "Describe the four success metrics in DFARS Appendix I-100(c), including the five-year measurement window after agreement completion.",
    "Distinguish the two participation mechanisms for Mentors—reimbursable and credit—and where each is governed in DFARS Appendix I."
]

# Document References
MPP_SOP_REFERENCES = [
    "1.1
2.1",
    "2.1
1.1",
    "6.3.2
6.3.3",
    "Chapter 7",
    "5.1.3
1.1"
]

APPENDIX_I_REFERENCES = [
    "I-100",
    "I-100
I-101",
    "I-106(d)
I-107",
    "I-100(c)
I-107(j)",
    "I-109
I-110.1
I-110.2"
]

# Lesson Summary (Generated using File Search)
LESSON_SUMMARY = """
This summary provides an overview of Module 1, Lesson 1, designed to equip MPP Program Managers with foundational knowledge of the Mentor-Protégé Program's (MPP) history, legal framework, operational mechanisms, and success measurement.

### 1. Brief Overview of This Lesson's Topic

This lesson provides an essential foundation for understanding the Department of Defense (DoD) Mentor-Protégé Program (MPP). It traces the program's evolution from its pilot phase in fiscal year 1991 to its current permanent standing under 10 U.S.C. § 4902. The core objective of the MPP is to incentivize major DoD contractors (Mentors) to assist eligible small business concerns (Protégés) in enhancing their capabilities to perform as subcontractors and suppliers, thereby increasing their participation in DoD, other federal, and commercial contracts. The lesson also highlights the importance of the Defense Federal Acquisition Regulation Supplement (DFARS) Appendix I as the implementing regulation, detailing how Mentor-Protégé Agreements (MPAs) are structured to achieve these developmental goals and how the program's success is measured.

### 2. Key Concepts and Requirements Covered

*   **Program Origins and Authority:** The MPP began as a "Pilot" program in FY1991 under Section 831 of Public Law 101-510, the National Defense Authorization Act (NDAA) for FY 1991. It was recently codified into permanent authority under 10 U.S.C. § 4902 by the NDAA 2023. DFARS Appendix I serves as the primary implementing regulation for the program.
*   **Purpose of Developmental Assistance:** The program aims to enhance the capabilities of eligible small businesses to perform as subcontractors and suppliers for DoD and other contracts. This is achieved through approved developmental assistance provided by Mentor firms to Protégé firms via MPAs. Developmental assistance is structured based on a preliminary assessment of the Protégé's needs and mutual agreement on the assistance to be provided. This assistance can include general business management, engineering and technical matters, acquisition or transfer of hardware/software/technology, and other support designed to develop the Protégé's capabilities. Developmental assistance must be distinct from normal subcontract administration and must contribute to DoD's mission or address a critical gap.
*   **MPA Structure:** MPAs are formalized agreements between Mentors and Protégés. Key elements include points of contact, NAICS codes, Protégé eligibility statements, and a detailed developmental assistance plan (DAP) outlining tasks, work breakdown structure, and milestones. The agreement must demonstrate how it contributes to the DoD mission.
*   **Success Metrics (DFARS Appendix I-100(c)):** The overall success of the MPP is measured by four key metrics, with a five-year measurement window after the completion of the agreement. These include:
    1.  An increase in the dollar value of contract and subcontract awards to Protégé firms (across DoD, other federal agencies, and commercial contracts).
    2.  An increase in the number and dollar value of subcontracts awarded to a Protégé (or former Protégé) by its Mentor (or former Mentor).
    3.  An increase in Protégé participation in DoD science and technology programs.
    4.  An increase in job creation of Protégé firms.
    Protégés are required to provide annual progress data on employment, revenues, and DoD contract participation during the program term and for two fiscal years following the agreement's expiration. DCMA also conducts annual performance reviews to verify reported data.
*   **Mentor Participation Mechanisms:** Mentors can participate in two primary ways:
    *   **Reimbursable Agreements (DFARS Appendix I-109):** Under this mechanism, the DoD reimburses the Mentor firm for approved developmental assistance costs. The military department or defense agency executes a contract modification or a separate contract before the Mentor incurs eligible costs. These agreements can include progress payments in excess of customary rates or advance payments if implemented per FAR guidance. Reimbursement for costs over $1M per fiscal year requires specific justification.
    *   **Credit Agreements (DFARS Appendix I-110, I-110.1, I-110.2):** Developmental assistance costs incurred by a Mentor under an approved credit agreement may be credited towards the Mentor firm's applicable subcontracting goals. This credit is treated as if the costs were incurred under a subcontract award to the Protégé. Unreimbursed costs for Protégés employing severely disabled individuals can be credited toward the Mentor's small disadvantaged business subcontracting goal. Credit agreements not associated with a specific DoD program or agency are submitted to the Director, OSBP, DCMA, for approval.

### 3. How These Objectives Relate to MPP Program Management

For MPP Program Managers, understanding these objectives is crucial for effective program execution and oversight:
*   **Compliance and Legal Basis:** PMs must be fully aware of the legal authority (10 U.S.C. § 4902) and implementing regulations (DFARS Appendix I) to ensure all program activities, agreements, and reporting are compliant.
*   **Agreement Development and Evaluation:** PMs utilize knowledge of developmental assistance purposes and MPA structural requirements (DFARS Appendix I-106(d), I-107) to evaluate proposals, ensuring they adequately address Protégé needs and align with DoD objectives. They must ensure that the proposed assistance is not duplicative of prior efforts and identifies planned developmental assistance based on a needs assessment.
*   **Performance Monitoring and Reporting:** The success metrics (DFARS Appendix I-100(c)) provide the framework for PMs to monitor the impact of MPAs, conduct quarterly reviews, and report progress. PMs must ensure Protégés submit required annual data for the program term and up to five years post-agreement. This data is essential for assessing ROI and overall program effectiveness.
*   **Financial Management and Incentives:** Distinguishing between reimbursable (DFARS Appendix I-109) and credit (DFARS Appendix I-110) mechanisms is critical for managing funding, understanding financial obligations, and accurately applying incentives for Mentors. PMs coordinate with various stakeholders, including DCMA, for review and approval of these agreements.

### 4. Practical Application Guidance

For MPP Program Managers, the following actions are recommended:
*   **Master the Regulatory Framework:** Regularly review 10 U.S.C. § 4902 and DFARS Appendix I to stay current with program policy and procedures. Maintain a comprehensive understanding of the requirements for MPA elements outlined in DFARS Appendix I-107.
*   **Emphasize Needs-Based Developmental Assistance:** During proposal evaluation, rigorously assess whether the proposed developmental assistance plan (DAP) is directly linked to a thorough needs assessment of the Protégé and aligns with the types of assistance authorized in DFARS Appendix I-106(d). Ensure the assistance contributes to the DoD mission.
*   **Implement Robust Performance Tracking:** Establish clear processes for collecting and analyzing the four success metrics outlined in DFARS Appendix I-100(c). Actively monitor Protégé performance for the full five-year post-agreement period, ensuring compliance with reporting requirements detailed in DFARS Appendix I-107(j) and I-112. Leverage annual performance reviews conducted by DCMA.
*   **Clarify Mentor Participation Early:** During outreach and proposal development, ensure Mentors clearly understand the implications and requirements of both reimbursable (DFARS Appendix I-109) and credit (DFARS Appendix I-110) agreements, including funding mechanisms, cost allowability, and reporting. Guide them on the appropriate submission process based on their chosen mechanism.
*   **Conduct Regular Reviews:** Utilize the quarterly agreement reviews (QARs) described in SOP Chapter 7 to monitor progress against milestones, discuss financial execution, identify and address issues, and collect success stories. Ensure DCMA and other relevant stakeholders are involved in reimbursable agreement QARs.
"""

def query_lesson_content(question: str) -> str:
    """
    Query MPP SOP and Appendix I documents for this lesson's content

    Args:
        question: Question about this lesson's topic

    Returns:
        Answer based on MPP documentation
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    file_search=types.FileSearch(
                        file_search_store_names=[FILE_SEARCH_STORE]
                    )
                )
            ]
        )
    )
    return response.text

def display_lesson_info():
    """Display lesson information"""
    print("=" * 80)
    print(f"Module 1 - Lesson 1")
    print("=" * 80)
    print("\nLEARNING OBJECTIVES:")
    for i, objective in enumerate(LEARNING_OBJECTIVES, 1):
        print(f"{i}. {objective}")

    print("\nDOCUMENT REFERENCES:")
    print(f"MPP SOP: {', '.join(MPP_SOP_REFERENCES)}")
    print(f"Appendix I: {', '.join(APPENDIX_I_REFERENCES)}")

    print("\nLESSON SUMMARY:")
    print(LESSON_SUMMARY)
    print("=" * 80)

if __name__ == "__main__":
    # Display lesson information
    display_lesson_info()

    # Interactive query mode
    print("\n🔍 Ask questions about this lesson (type 'exit' to quit):\n")

    while True:
        question = input("Question: ").strip()

        if question.lower() in ['exit', 'quit', 'q']:
            print("Goodbye!")
            break

        if not question:
            continue

        print("\n📖 Searching MPP documents...\n")
        answer = query_lesson_content(question)
        print(f"Answer:\n{answer}\n")
        print("-" * 80 + "\n")
