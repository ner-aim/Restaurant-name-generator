# -*- coding: utf-8 -*-
"""
Created on Wed May 14 17:52:38 2025

@author: sid99
"""
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
import os

os.environ['OPENAI_API_KEY'] = 'skQA'
    
llm = OpenAI(temperature = 0.9)




def generate_restaurant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for the restaurant."
        )
    name_chain = LLMChain(llm=llm, prompt = prompt_template_name, output_key = "restaurant_name")

    prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template = "Suggest some menu items for {restaurant_name}. Return it as a comma separated list"
                )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key = "menu_items")
    
    chain = SequentialChain(chains = [name_chain, food_items_chain], input_variables = ["cuisine"], output_variables = ["restaurant_name", "menu_items"])
    response = chain({'cuisine':cuisine})
    
    return response

if __name__ == "__main__":
    print (generate_restaurant_name_and_items("Japanese"))