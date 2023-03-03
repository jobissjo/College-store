let msg_element = document.getElementById("msgs");
//let show_details = document.getElementById("show_details_form")
////let temp_btn = document.querySelector(".temp_btn")
//let form_container = document.querySelector(".form-container")
//const departmentDropdown = document.querySelector('#id_department');
//const coursesDropdown = document.querySelector('#id_courses');


setTimeout(function(){
    msg_element.style.display = "none"
}, 3000)

//show_details.addEventListener('click', function(){
//    console.log("hello")
//    temp_btn.remove();
//    form_container.style.display = "block"
//})
//departmentDropdown.addEventListener('change', handleDepartmentChange);

//function handleDepartmentChange() {
//  const departmentId = this.value;
//  fetch(`/api/courses/?department_id=${departmentId}`)
//    .then(response => response.json())
//    .then(courses => {
//      coursesDropdown.innerHTML = '';
//      courses.forEach(course => {
//        const option = document.createElement('option');
//        option.value = course.id;
//        option.textContent = course.name;
//        coursesDropdown.appendChild(option);
//      });
//    });
//}