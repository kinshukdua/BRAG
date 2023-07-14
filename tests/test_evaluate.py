from evaluate import evaluate_rag

def test_evaluation():
    ctx_score, ans_score = evaluate_rag("What is PAN?",
                 "The PAN card is a unique ten-digit alphanumeric identification number",
                 """# About Pan Card

                    ### What is Pan card?

                    The PAN card is a unique ten-digit alphanumeric identification number that is issued by the Income Tax Department of India to track the tax-related transactions of individuals and entities.""")
    assert ctx_score>0.85 and ans_score >0.85