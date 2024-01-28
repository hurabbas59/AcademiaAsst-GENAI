import streamlit as st
import requests
url = "http://127.0.0.1:7000/"
def main():
    st.title("Acadamia Assistant")

    # Function to upload JSON file for course outline
    def upload_outline_file():
        st.subheader("1. Course Outline Generation")
        uploaded_file = st.file_uploader("Upload JSON file for course outline", type=["json"])
        
        if uploaded_file is not None:
            payload = {
              "file":uploaded_file.name
            }
            
            response = requests.post(url=url+"generate_course_modules",json=payload)
            st.success("Course outline generated successfully!")

    # Function to generate exam for a given subject
    def generate_exam_for_subject():
        st.subheader("2. Exam Generation")
        name = st.text_input("Enter your name:")
        
        # Dropdown for course type
        course_type = st.selectbox("Select Course Type", ["Technical", "Theoretical"])

        # Dropdown for difficulty level
        difficulty = st.selectbox("Select Difficulty Level", ["Easy", "Intermediate", "Hard"])

        # Dropdown for exam time
        exam_time = st.selectbox("Select Exam Time", ["30 minutes", "60 minutes", "90 minutes", "120 minutes"])

        semesters = st.text_input("Enter number of semesters")

        # Optional topics input
        topics = st.text_input("Topics to include (optional):")

        if st.button("Generate Exam"):
            
            exam_request_payload = {
                "course_name": name,
                "course_type": course_type,
                "difficulty_level": difficulty,
                "exam_time": exam_time,
                "semester": semesters,
                "topics_to_include": topics
            }
            print(exam_request_payload)
            
            response = requests.post(url=url+"generate_exam",json=exam_request_payload)

            st.success("Exam generated successfully!")

    # Function to generate content for a given subject
    def generate_content_for_subject():
      st.subheader("3. Content Generation")

      # Fields for user input
      subject_name_content = st.text_input("Enter subject name for content generation:")
      course_type = st.selectbox("Select course type:", ["Technical", "Theoretical"])
      semester = st.number_input("Enter semester (1-8):", min_value=1, max_value=8)

      if st.button("Generate Content"):
          module_content_request_payload = {
                "course_type": course_type,
                "course_title": subject_name_content,
                "semester": semester
            }
          response = requests.post(url=url + "generate_content" , json=module_content_request_payload ) 
          
          
          # Display success message
          st.success("Content generated successfully!")


    # Sidebar navigation
    menu_option = st.sidebar.radio("Select Functionality", ["Home", "Course Outline", "Generate Exam", "Generate Content"])

    if menu_option == "Home":
        st.write("Welcome to the Course Management App!")

    elif menu_option == "Course Outline":
        upload_outline_file()

    elif menu_option == "Generate Exam":
        generate_exam_for_subject()

    elif menu_option == "Generate Content":
        generate_content_for_subject()

if __name__ == "__main__":
    main()
