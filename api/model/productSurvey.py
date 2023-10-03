productDecisionTree = {
    "STEP1": {
        "question": "Did you purchase something?",
        "next": {
            "yes": "STEP2",
            "no": "FINAL",
        },
        "needResponse": True,
        "needButton": True
    },
    "STEP2": {
        "question": "Would you be open to leaving feedback to improve our product?",
        "next": {
            "yes": "STEP3",
            "no": "FINAL",
        },
        "needResponse": True,
        "needButton": True
    },
    "STEP3": {
        "question": "How would you rate the product you purchased from 1-5?",
        "next": "STEP4",
        "record": True,
        "needResponse": True,
        "needButton": False,
        "needRating": True
    },
    "STEP4": {
        "question": "Do you have any feedback?",
        "next": "STEP5",
        "record": True,
        "needResponse": True,
        "needButton": False,
        "needForm": True
    },
    "STEP5": {
        "question": "Thank you for your feedback!",
        "needResponse": False,
        "needButton": False,
    },
    "FINAL": {
        "question": "Thank you for your purchase!",
        "needResponse": False,
        "needButton": False,
    }
}