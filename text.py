import streamlit as st

st.title('Text Analyzer 📊')
st.write('This is a simple text analyzer that counts words, characters, spaces, vowels, and allows word replacement. ✍️') 

# User Input
text = st.text_area('Enter text here 📝')

if st.button('Analyze 🔍'):
    if text.strip():  # Check if text is not empty
        word_count = len(text.split())
        char_count = len(text)
        space_count = text.count(' ')
        vowels = 'aeiouAEIOU'
        vowel_count = sum(1 for char in text if char in vowels)

        st.write(f'**Total Words:** {word_count} 📝')
        st.write(f'**Total Characters:** {char_count} 🔠')
        st.write(f'**Total Spaces:** {space_count} 🚀')
        st.write(f'**Total Vowels:** {vowel_count} 💬')
        st.write(f'**Uppercase:** {text.upper()} 🔠')
        st.write(f'**Lowercase:** {text.lower()} 🔡')
    else:
        st.warning('Please enter some text before analyzing! ⚠️')

# Word Replacement
search_word = st.text_input('Enter the word to search for 🔍')
replace_word = st.text_input('Enter the word to replace it with 🔄')    

if st.button('Replace Word'):
    if text and search_word and replace_word:
        if search_word in text:
            new_text = text.replace(search_word, replace_word)
            st.write(f'**New Text Generated:** {new_text} ✏️')
        else:
            st.warning(f'The word "{search_word}" was not found in the text. ❌')
    else:
        st.warning('Please enter text and words for replacement. ⚠️')

st.write('Made with ❤️ by Shabana')
