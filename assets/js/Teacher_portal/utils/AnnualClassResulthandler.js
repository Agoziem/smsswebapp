class AnnualClassResultHandler {
    constructor(data) {
      this.students = data;
      this.calculateFields();
    }
  
    calculateFields() {
      this.students.forEach((student) => {
        student.Total = this.calculateTotal(student);
        student.Average = this.calculateAverage(student);
        student.Grade = this.calculateGrade(student);
        student.Position = "-";
        student.Remarks = "-";
        student.Verdict = "-";
      });
  
      // Calculate position based on Total
      this.calculatePosition();
  
      // Calculate remarks based on Grade
      this.calculateRemarks();

      // Calculate Verdict based on Grade
      this.declareVerdict();
    }
  
    // this has to be Calulated dynamically
    calculateTotal(student) {
      const keys = Object.keys(student);
      const startIndex = keys.indexOf("Name") + 1;
      const endIndex = keys.indexOf("published");
      const relevantKeys = keys.slice(startIndex, endIndex);
      return relevantKeys.reduce(
        (sum, key) =>
          sum +
          (isNaN(student[key]["Average"]) ? 0 : parseInt(student[key]["Average"])),
        0
      );
    }
  
    // this has to be Calulated dynamically
    calculateAverage(student) {
      const keys = Object.keys(student);
      const startIndex = keys.indexOf("Name") + 1;
      const endIndex = keys.indexOf("published");
      const relevantKeys = keys.slice(startIndex, endIndex);
      const greaterThanOrEqualToOneCount = relevantKeys.filter(
        (key) =>
          parseInt(student[key]["Average"]) >= 0 && student[key]["Average"] !== "-"
      ).length;
      // Check if greaterThanOrEqualToOneCount is not zero before performing the division
      const average =
        greaterThanOrEqualToOneCount !== 0
          ? parseFloat((student.Total / greaterThanOrEqualToOneCount).toFixed(2))
          : 0;
  
      return average;
    }
  
    calculateGrade(student) {
      if (student.Average >= 70) return "A";
      else if (student.Average >= 55) return "C";
      else if (student.Average >= 40) return "P";
      else return "F";
    }
  
    calculatePosition() {
      this.students.sort((a, b) => b.Average - a.Average);
  
      // Function to calculate ordinal suffix
      const getOrdinalSuffix = (number) => {
        if (number === 11 || number === 12 || number === 13) {
          return "th";
        } else {
          const lastDigit = number % 10;
          switch (lastDigit) {
            case 1:
              return "st";
            case 2:
              return "nd";
            case 3:
              return "rd";
            default:
              return "th";
          }
        }
      };
  
      let previousAverage = null;
      let previousPosition = null;
  
      this.students.forEach((student, index) => {
        const currentTotal = student.Average;
        const suffix = getOrdinalSuffix(index + 1);
  
        if (currentTotal === previousAverage) {
          // Assign the same position as the previous student
          student.Position = previousPosition;
        } else {
          // Assign a new position
          student.Position = `${index + 1}${suffix}`;
        }
  
        // Update previous total and position
        previousAverage = currentTotal;
        previousPosition = student.Position;
      });
    }
  
    calculateRemarks() {
      this.students.forEach((student) => {
        if (student.Grade === "-") student.Remarks = "-";
        else if (student.Grade === "A") student.Remarks = "Excellent";
        else if (student.Grade === "C") student.Remarks = "Good";
        else if (student.Grade === "P") student.Remarks = "Pass";
        else student.Remarks = "Fail";
      });
    }

    declareVerdict(){
      this.students.forEach((student) => {
        if (student.Grade === "-") student.Verdict = "-";
        else if (student.Grade === "A") student.Verdict = "Promoted";
        else if (student.Grade === "C") student.Verdict = "Promoted";
        else if (student.Grade === "P") student.Verdict = "Promoted";
        else student.Verdict = "Not Promoted";
    })
    }

    getStudents() {
      return this.students;
    }
  }
  
  export default AnnualClassResultHandler;
  