import pytest

from deepeval.dataset import EvaluationDataset
from deepeval import assert_test, evaluate
from deepeval.test_case import MLLMTestCase, LLMTestCase, MLLMImage
from deepeval.metrics import (
    AnswerRelevancyMetric,
    ImageEditingMetric,
    TextToImageMetric,
    MultimodalContextualRecallMetric,
    MultimodalContextualRelevancyMetric,
)

image_path = "./data/image.webp"
edited_image_path = "./data/edited_image.webp"

#############################################################
# TestCases
#############################################################

text_to_image_test_case = MLLMTestCase(
    input=[
        "gesnerate a castle school in fantasy land with the words LLM evaluation on it"
    ],
    actual_output=[MLLMImage(image_path, local=True)],
)

image_editing_test_case = MLLMTestCase(
    input=[
        "edit this image so that it is night themed, and LLM evaluation is spelled correctly",
        MLLMImage(image_path, local=True),
    ],
    actual_output=[MLLMImage(edited_image_path, local=True)],
)

llm_test_case = LLMTestCase(
    input="What is this again?",
    actual_output="this is a latte",
    expected_output="this is a mocha",
    retrieval_context=["I love coffee"],
    context=["I love coffee"],
    expected_tools=["mixer", "creamer", "dripper"],
    tools_called=["mixer", "creamer", "mixer"],
)

contextual_recall_test_case = image_editing_test_case = MLLMTestCase(
    input=["Tell me about some landmarks in France"],
    actual_output=[""],
    expected_output=[
        "The Eiffel Tower is located in Paris, France.",
        MLLMImage(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg/375px-Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg"
        ),
        "The Statue of Liberty was a gift from France to the United States.",
        MLLMImage(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Front_view_of_Statue_of_Liberty_with_pedestal_and_base_2024.jpg/375px-Front_view_of_Statue_of_Liberty_with_pedestal_and_base_2024.jpg"
        ),
    ],
    context=[
        "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris.",
        "It is named after the engineer Gustave Eiffel.",
        MLLMImage(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg/375px-Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg"
        ),
        "The Statue of Liberty is a colossal neoclassical sculpture on Liberty Island in New York Harbor.",
        MLLMImage(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Liberty-from-behind-2024.jpg/330px-Liberty-from-behind-2024.jpg"
        ),
    ],
    retrieval_context=[
        "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris.",
        "It is named after the engineer Gustave Eiffel.",
        MLLMImage(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg/375px-Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg"
        ),
        "The Statue of Liberty is a colossal neoclassical sculpture on Liberty Island in New York Harbor.",
        MLLMImage(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Liberty-from-behind-2024.jpg/330px-Liberty-from-behind-2024.jpg"
        ),
    ],
)


#############################################################
# Evaluate
#############################################################

metric = MultimodalContextualRelevancyMetric(verbose_mode=True)
score = metric.measure(contextual_recall_test_case)

# dataset = EvaluationDataset(
#     test_cases=[
#         # text_to_image_test_case,
#         image_editing_test_case,
#         llm_test_case
#     ]
# )
# dataset.evaluate(
#     [
#         # TextToImageMetric(),
#         ImageEditingMetric(),
#         AnswerRelevancyMetric(),
#     ]
# )

# evaluate(
#     test_cases=[
#         text_to_image_test_case,
#         # image_editing_test_case,
#         llm_test_case,
#     ],
#     metrics=[
#         TextToImageMetric(),
#         # ImageEditingMetric(),
#         AnswerRelevancyMetric(),
#     ],
# )
