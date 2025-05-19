import streamlit as st
import os 
from src.utils import load_model, apply_skill, apply_skills, convert_newlines
from src.prompts import insert
from src.languages import LANGUAGES

# Set page config first
st.set_page_config(page_title="Prompt Enhancer", page_icon=":rocket:", initial_sidebar_state="collapsed", layout="wide")

# Language selection with flags
language_options = {
    "en": "🇺🇸 English",
    "vi": "🇻🇳 Tiếng Việt"
}
language = st.sidebar.selectbox("Language / Ngôn ngữ", list(language_options.keys()), format_func=lambda x: language_options[x], index=0)
lang = LANGUAGES[language]

# Update page title after language selection
st.title(f":rocket: {lang['title']}")
st.markdown(f"""
##### {lang['subtitle']}
""")
st.text("")
st.text("")

with st.popover(f"**:blue[{lang['api_key_title']}]**"):
    OPENAI_API_KEY = st.text_input(lang['api_key_placeholder'], type="password")
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY 
    st.info(f"""
    {lang['api_key_info']} [{lang['here']}](https://platform.openai.com/api-keys)
    """)

temp, buff = st.columns([0.3, 0.7]) 
if not OPENAI_API_KEY:
    temp.error(f"**{lang['api_key_error']}**") 
st.text("")
st.text("")

col1, buff, col2 = st.columns([0.3, 0.05, 0.65])

with col1:
    st.markdown(f"""### {lang['skills_title']}""")
    with st.popover(f"**:blue[{lang['learn_more']}]**"):
        st.info(f"{lang['skills_info']} [{lang['here']}](https://phontron.com/class/anlp-fall2024/assets/slides/anlp-07-prompting.pdf)")
        st.warning(f"**{lang['skills_warning']}**")
    
    toggle_all = st.toggle(f"**{lang['select_all']}**", key="master_toggle")
    
    with st.expander(f"**{lang['prompt_structure']}**", expanded=True):
        audience_integration = st.toggle(f"**{lang['audience_integration_title']}**", value=toggle_all)
        st.markdown(lang['audience_integration_desc'])
        affirmative_sentencing = st.toggle(f"**{lang['affirmative_sentencing_title']}**", value=toggle_all)
        st.markdown(lang['affirmative_sentencing_desc'])
        output_primers = st.toggle(f"**{lang['output_primers_title']}**", value=toggle_all)
        st.markdown(lang['output_primers_desc'])
        delimiters = st.toggle(f"**{lang['delimiters_title']}**", value=toggle_all) 
        st.markdown(lang['delimiters_desc'])
        formatted_prompt = st.toggle(f"**{lang['formatted_prompt_title']}**", value=toggle_all) 
        st.markdown(lang['formatted_prompt_desc'])

    with st.expander(f"**{lang['specificity']}**", expanded=True):
        fewshot_prompting = st.toggle(f"**{lang['fewshot_prompting_title']}**", value=toggle_all)
        st.markdown(lang['fewshot_prompting_desc'])
        guideline_indicators = st.toggle(f"**{lang['guideline_indicators_title']}**", value=toggle_all)
        st.markdown(lang['guideline_indicators_desc'])

    with st.expander(f"**{lang['content_style']}**", expanded=True): 
        no_politeness = st.toggle(f"**{lang['no_politeness_title']}**", value=toggle_all)
        st.markdown(lang['no_politeness_desc'])
        imperative_task = st.toggle(f"**{lang['imperative_task_title']}**", value=toggle_all)
        st.markdown(lang['imperative_task_desc'])
        penalty_warning = st.toggle(f"**{lang['penalty_warning_title']}**", value=toggle_all) 
        st.markdown(lang['penalty_warning_desc'])
        role_assignment = st.toggle(f"**{lang['role_assignment_title']}**", value=toggle_all)
        st.markdown(lang['role_assignment_desc'])
        echo_directive = st.toggle(f"**{lang['echo_directive_title']}**", value=toggle_all)
        st.markdown(lang['echo_directive_desc'])
    
    with st.expander(f"**{lang['complex_tasks']}**", expanded=True): 
        task_decomposition = st.toggle(f"**{lang['task_decomposition_title']}**", value=toggle_all)
        st.markdown(lang['task_decomposition_desc'])

    skills_to_apply = {
        "no_politeness": no_politeness, 
        "affirmative_sentencing": affirmative_sentencing,  
        "audience_integration": audience_integration,
        "role_assignment": role_assignment,
        "penalty_warning": penalty_warning,
        "imperative_task": imperative_task,
        "guideline_indicators": guideline_indicators,
        "task_decomposition": task_decomposition,
        "fewshot_prompting": fewshot_prompting,
        "echo_directive": echo_directive,
        "delimiters": delimiters,
        "formatted_prompt": formatted_prompt,
        "output_primers": output_primers,
    }

with col2:
    st.markdown(f"""### {lang['enhance_title']}""")
    st.text("")
    prompt = st.text_area(f"**{lang['original_prompt']}**", placeholder=lang['prompt_placeholder'], height=300)

    phrases_to_insert = {} 
    st.text("")
    st.markdown(f"**{lang['magical_phrases']}**")
    step_by_step = st.checkbox(lang['step_by_step'])
    tipping = st.checkbox(lang['tipping'])
    important_to_career = st.checkbox(lang['important_to_career'])
    explain_beginner = st.checkbox(lang['explain_beginner'])
    detailed_writing = st.checkbox(lang['detailed_writing'])
    human_like_response = st.checkbox(lang['human_like_response'])
    unbiased_response = st.checkbox(lang['unbiased_response'])
    
    phrases_to_insert = {
        "step_by_step": step_by_step,
        "tipping": tipping,
        "important_to_career": important_to_career,
        "explain_beginner": explain_beginner,
        "detailed_writing": detailed_writing,
        "human_like_response": human_like_response,
        "unbiased_response": unbiased_response,
    }

    st.text("")

    model_name = st.selectbox(f"**{lang['select_model']}**", 
                              ("gpt-4o", "chatgpt-4o-latest", "gpt-4o-mini", "gpt-4-turbo", "gpt-4-0125-preview"), 
                              index=0, 
                              placeholder="Select the model...")

    st.text("") 

    lang_eng = st.checkbox(f"**{lang['english_option']}**")
    simplified = st.checkbox(f"**{lang['simplified_option']}**")
    st.text("")
    st.text("")
    enhance_btn = st.button(f"**:blue[{lang['enhance_button']}]**")

    if enhance_btn:
        if not prompt:
            st.toast(lang['enter_prompt'])
        if not OPENAI_API_KEY:
            st.toast(lang['api_key_error'])

        order_num = 1
        with st.spinner(lang['processing']): 
            llm = load_model(model_name)

            if simplified:
                prompt = apply_skills(llm, skills_to_apply, prompt, lang_eng) 
                
                for phrase, checked in phrases_to_insert.items():
                    if checked:
                        prompt = insert[phrase] + '\n' + prompt
    
            else:
                for skill, toggled in skills_to_apply.items():
                    if toggled:
                        prompt = apply_skill(llm, skill, prompt, order_num, lang_eng)
                        st.markdown(f":zap: {order_num}. {lang['enhancement_skill'].format(skill=skill)}")
                        container = st.container(border=True)
                        container.markdown(convert_newlines(prompt))
                        order_num+=1

                for phrase, checked in phrases_to_insert.items():
                    if checked:
                        st.markdown(f":zap: {order_num}. {lang['enhancement_phrase'].format(phrase=phrase)}")
                        prompt = insert[phrase] + '\n' + prompt
                        container = st.container(border=True)
                        container.markdown(convert_newlines(prompt)) 
                        order_num+=1
                
        st.toast(lang['enhancement_success'])     
        st.markdown(f"### {lang['enhanced_prompt']}")
        container = st.container(border=True)
        container.title(":crystal_ball:")
        container.markdown(convert_newlines(prompt)) 

st.text("")
st.text("")
# st.markdown(f"<p style='text-align: center;'>{lang['contact_email']}</p>", unsafe_allow_html=True)
# st.markdown(f"<p style='text-align: center;'>{lang['contact_github']}</p>", unsafe_allow_html=True)