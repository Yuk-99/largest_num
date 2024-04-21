import streamlit as st
def largest(x,y,z):
  return max(x,y,z)

def main():
  st.title("To find the largest value")
  st.write("Enter the numbers")

  n1 = st.number_input("Enter number here", value=0)
  n2 = st.number_input("Enter number here", value=0)
  n3 = st.number_input("Enter number here", value=0)

  if st.button("Compare"):
    answer = largest(n1,n2,n3)
    st.write("The largest among the three numbers is {answer}")

if __name__ == "__main__":
  main()   
