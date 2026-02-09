import pytest
import allure
from data.test_data import TestDataQuestions


@allure.feature("Вопросы о важном")
@allure.story("Проверка выпадающего списка вопросов")
class TestQuestions:
    
    @pytest.mark.parametrize("question_data", TestDataQuestions.QUESTIONS_AND_ANSWERS)
    def test_question_dropdown(self, main_page, question_data):

        with allure.step(f"Проверка вопроса: {question_data['question']}"):
            question_index = None
            for i, qa in enumerate(TestDataQuestions.QUESTIONS_AND_ANSWERS):
                if qa["question"] == question_data["question"]:
                    question_index = i
                    break
            
            assert question_index is not None, f"Вопрос не найден: {question_data['question']}"
            
            main_page.click_question(question_index)
            
            actual_answer = main_page.get_answer_text(question_index)
            
            assert actual_answer == question_data["answer"], \
                f"Ожидался ответ: {question_data['answer']}, получен: {actual_answer}"
    
    @allure.title("Проверка всех вопросов последовательно")
    def test_all_questions_in_sequence(self, main_page):

        for i in range(len(TestDataQuestions.QUESTIONS_AND_ANSWERS)):
            with allure.step(f"Проверка вопроса {i+1}"):
                question_data = TestDataQuestions.QUESTIONS_AND_ANSWERS[i]
                
                main_page.click_question(i)
                
                actual_answer = main_page.get_answer_text(i)
                
                assert actual_answer == question_data["answer"], \
               f"Вопрос {i+1}: ожидался '{question_data['answer']}', получен '{actual_answer}'"