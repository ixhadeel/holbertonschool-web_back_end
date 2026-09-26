export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const studentGrade = newGrades.find(
        (grade) => grade.studentId === student.id
      );

      let grade = 'N/A';

      if (studentGrade) {
        grade = studentGrade.grade;
      }

      return {
        ...student,
        grade,
      };
    });
}