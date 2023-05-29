import  streamlit   as  st
from streamlit_option_menu import option_menu
import base64
from main  import   main
from main2 import main2 
from streamlit_image_select import image_select  
st.set_page_config(page_title="Your Online Yoga Trainer",page_icon="🌄",layout="wide")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
 

# 2. horizontal menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "About","Practice",'Seated Yoga Poses','Standing Yoga Poses','Forward Bend Yoga Poses','Back Bend Yoga Poses','Twist Yoga Poses','Inversion Yoga Poses','Restorative Yoga Poses','Preparatory Yoga Poses','Contact'], 
    icons=['house',"person lines fill", 'book',"list-task","list-task",'list-task','list-task','list-task','list-task','list-task','list-task', 'envelope'], 
    menu_icon="cast", default_index=0)
    

if selected=="Home":
    add_bg_from_local('bg2.jpg')  
    st.subheader('Welcome To Your Online Yoga Trainer')
    st.title("What hurts today makes you stronger tomorrow")
    

elif selected=="About":
    st.title("Personal guidance at your convenience")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:         
            st.subheader(
                """
                Step in to a connected Yoga practice by simply placing your device 4-5 feet away and stepping on your mat.Tracks 12 key-points on your body with your device and provides you feedback to correct your yoga pose based on rule generated by calculating 8 angles between extracted key point.
                """
            )   
        with right_column:
            st.image("bg4.jpg",width=400)
     
           
elif  selected== "Seated Yoga Poses":
    st.title("Seated Yoga Poses")
    img = image_select(
    label="Select Yoga you  want  to  TRY!",
    images=[
        "Seated/1.jpg","Seated/2.jpg","Seated/3.jpg","Seated/4.jpg","Seated/5.jpg","Seated/6.jpg",
        "Seated/7.jpg","Seated/8.jpg","Seated/9.jpg","Seated/10.jpg","Seated/11.jpg","Seated/12.jpg"       
    ],
    captions=["1.Padmasana", "2.Sukhasana", "3.Baddha Konasana", "4.Gomukhasana","5.Virasana","6.Dandasana",
              "7.Krounchasana","8.Vajrasana","9.Navasana","10.Surya Yantrasana","11.Hanumanasana","12.Ardha Kapotasana"],
)
    if st.button("Let's Start"):
        main(path=img)


elif  selected== "Standing Yoga Poses":
    st.title("Standing Yoga Poses")
    img = image_select(
    label="Select Yoga you  want  to  TRY!",
    images=[
        "Standing/Utthita Trikonasana.jpg","Standing/tpose.jpg","Standing/Parivrtta Trikonasana.jpg","Standing/Tadasana.jpg","Standing/Urdhva Hastasana.jpg","Standing/Ardha Uttanasana.jpg","Standing/Utkatasana.jpg",
        "Standing/Virabhadrasana I.jpg","Standing/Virabhadrasana II.jpg","Standing/Utthita Parsvakonasana.jpg","Standing/Vrksasana.jpg","Standing/Utthita Hasta Padangusthasana A.jpg","Standing/Utthita Hasta Padangusthasana B.jpg" ,
        "Standing/Ardha Chandrasana.jpg", "Standing/Garudasana.jpg"   , "Standing/Natarajasana.jpg"   , "Standing/Baddha Parsvakonasana.jpg"    ,"Standing/Ardha Padma Vrksasana.jpg","Standing/Utthita ashwa sanchalanasana.jpg","Standing/Ashwa sanchalanasana.jpg","Standing/Virabhadrasana III.jpg"    
    ],
    captions=["1.Utthita Trikonasana", "T POSE", "2.Parivrtta Trikonasana", "3.Tadasana", "4.Urdhva Hastasana","5.Ardha Uttanasana","6.Utkatasana",
              "7.Virabhadrasana I","8.Standing/Virabhadrasana II","9.Utthita Parsvakonasana","10.Vrksasana","11.Utthita Hasta Padangusthasana A","12.Utthita Hasta Padangusthasana B",
              "Ardha Chandrasana","Garudasana","Natarajasana","Baddha Parsvakonasana","Ardha Padma Vrksasana","Utthita ashwa sanchalanasana","Ashwa sanchalanasana","Virabhadrasana III"],
)
    if st.button("Let's Start"):
        main(path=img)


elif  selected== "Forward Bend Yoga Poses":
    st.title("Forward Bend Yoga Poses")
    img = image_select(
    label="Select Yoga you  want  to  TRY!",
    images=[
        "Forward Bend/Uttanasana.jpg","Forward Bend/Janu Sirsasana.jpg","Forward Bend/Marichyasana I.jpg","Forward Bend/Upavistha Konasana.jpg","Forward Bend/Parsvottanasana.jpg","Forward Bend/Ardha Baddha Padmottanasana.jpg",
        "Forward Bend/Baddha Padmasana.jpg","Forward Bend/Parsvottanasana Paschima Namaskarasana.jpg","Forward Bend/Paschimottanasana.jpg"       
    ],
    captions=["1.Uttanasana", "2.Janu Sirsasana", "3.Marichyasana I", "4.Upavistha Konasana","5.Parsvottanasana","6.Ardha Baddha Padmottanasana",
              "7.Baddha Padmasana","8.Parsvottanasana Paschima Namaskarasana","9.Paschimottanasana"],
)
    if st.button("Let's Start"):
        main(path=img)


elif  selected== "Back Bend Yoga Poses":
    st.title("Back Bend Yoga Poses")
    img = image_select(
    label="Select Yoga you  want  to  TRY!",
    images=[
        "Back Bend/Bhujangasana.jpg","Back Bend/Dhanurasana.jpg","Back Bend/Eka Pada Rajakapotasana.jpg","Back Bend/Ustrasana.jpg","Back Bend/Sethu Bandha Sarvangasana.jpg","Back Bend/Supta Virasana.jpg",
        "Back Bend/Matsyasana.jpg","Back Bend/Hasta Uttanasana.jpg","Back Bend/Camatkarasana.jpg", "Back Bend/Urdhva dhanurasana.jpg"  
    ],
    captions=["1.Bhujangasana", "2.Dhanurasana", "3.Eka Pada Rajakapotasana", "4.Ustrasana","5.Sethu Bandha Sarvangasana","6.Supta Virasana",
              "7.Matsyasana","8.Hasta Uttanasana","9.Camatkarasana","10.Urdhva dhanurasana"],
)
    if st.button("Let's Start"):
        main(path=img)


elif  selected== "Twist Yoga Poses":
    st.title("Twist Yoga Poses")
    img = image_select(
    label="Select Yoga you  want  to  TRY!",
    images=[
        "Twist/Ardha Matsyendrasana.jpg","Twist/Marichyasana III.jpg","Twist/Supta Matsyendrasana.jpg","Twist/Parivrtta Janu Sirsasana.jpg","Twist/Matsyendrasana.jpg"
    ],
    captions=["1.Ardha Matsyendrasana", "2.Marichyasana III", "3.Supta Matsyendrasana", "4.Parivrtta Janu Sirsasana","5.Matsyendrasana"],
)
    if st.button("Let's Start"):
        main(path=img)


elif  selected== "Inversion Yoga Poses":
    st.title("Inversion  Yoga Poses")
    img = image_select(
    label="Select Yoga you  want  to  TRY!",
    images=[
        "Inversion/Adho Mukha Svanasana.jpg","Inversion/Halasana.jpg","Inversion/Sarvangasana.jpg","Inversion/Sirsasana.jpg","Inversion/Urdhva Dandasana.jpg","Inversion/Padma Sarvangasana.jpg",
        "Inversion/Matsyasana variation.jpg","Inversion/Salamba Sirsasana.jpg"  
    ],
    captions=["1.Adho Mukha Svanasana", "2.Halasana", "3.Sarvangasana", "4.Sirsasana","5.Urdhva Dandasana","6.Padma Sarvangasana",
              "7.Matsyasana variation","8.Salamba Sirsasana"],
)
    if st.button("Let's Start"):
        main(path=img)


elif  selected== "Restorative Yoga Poses":
    st.title("Restorative Yoga Poses")
    img = image_select(
    label="Select Yoga you  want  to  TRY!",
    images=[
        "Seated/1.jpg","Seated/2.jpg","Seated/3.jpg","Seated/4.jpg","Seated/5.jpg","Seated/6.jpg",
        "Seated/7.jpg","Seated/8.jpg","Seated/9.jpg","Seated/10.jpg","Seated/11.jpg","Seated/12.jpg"       
    ],
    captions=["1.Padmasana", "2.Sukhasana", "3.Baddha Konasana", "4.Gomukhasana","5.Virasana","6.Dandasana",
              "7.Krounchasana","8.Vajrasana","9.Navasana","10.Surya Yantrasana","11.Hanumanasana","12.Ardha Kapotasana"],
)
    if st.button("Let's Start"):
        main(path=img)


elif  selected== "Restorative Yoga Poses":
    st.title("Restorative Yoga Poses")
    img = image_select(
    label="Select Yoga you  want  to  TRY!",
    images=[
        "Restorative/Balasana.jpg","Restorative/Shavasana.jpg","Restorative/Supta Baddha konasana.jpg" ],
    captions=["1.Balasana", "2.Shavasana", "3.Supta Baddha konasana"],
)
    if st.button("Let's Start"):
        main(path=img)


elif  selected== "Preparatory Yoga Poses":
    st.title("Preparatory Yoga Poses")
    img = image_select(
    label="Select Yoga you  want  to  TRY!",
    images=[
        "Preparatory/Malasana.jpg","Preparatory/Bharmanasana.jpg","Preparatory/Bitilasana.jpg","Preparatory/Marjariasana.jpg"],
    captions=["1.Malasana", "2.Bharmanasana", "3.Bitilasana", "4.Marjariasana"],
)
    if st.button("Let's Start"):
        main(path=img)


elif selected=="Practice":
    st.title("Seated Yoga Poses")
    with st.container():
        st.write("---")
        st.header('Lotus Pose')
        
        col1, col2 = st.columns(2)
        with col1:
           
            st.image("Seated/1.jpg",width=400)
            
        with col2:
            st.subheader("Sanskrit Name: Padmasana")
            st.subheader("Benefits:")
            st.write(
                """
                Lotus Pose is great for meditation and Pranayama practice. Much more stable than its counterparts. 
                This asana allows the entire body to remain steady during a long period of time. Hip Opening, Relaxing, Improving Posture.
                """
            )
            st.subheader("Keys:")
            st.write(
                """
                Feet on the top of thighs, Spine elongate, mind the knees, and relax the shoulders. 
                Top of the head toward the ceiling and chin slightly down. A great mobility in the hips are required before mastering the pose.
                """
            )
            st.subheader("Cautions: ")
            st.write(" Any pain or injuries in the knees, ankles or calves.")
            st.subheader("Level: Intermediate")    
    if st.button('Start'):
        main(path="Seated/1.jpg")


elif selected=="Contact":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contact Form</p>', unsafe_allow_html=True)
    with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
        Name=st.text_input(label='Please Enter Your Name') #Collect user feedback
        Email=st.text_input(label='Please Enter Email') #Collect user feedback
        Message=st.text_input(label='Please Enter Your Message') #Collect user feedback
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
                            