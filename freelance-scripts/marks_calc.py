def calculate_student_percentage():
    """
    International Student Marks Percentage Calculator
    Supports different grading systems worldwide
    """
    print("📚 International Student Percentage Calculator")
    print("=" * 50)
    
    # Flexible system for different countries
    try:
        subjects = int(input("Number of subjects (default 3): ") or "3")
        max_marks = float(input("Maximum marks per subject (default 100): ") or "100")
    except ValueError:
        subjects, max_marks = 3, 100.0
        print("Using defaults: 3 subjects, 100 marks each")
    
    print(f"\n📝 Enter marks for {subjects} subjects (0-{max_marks}):")
    
    # Collect marks with validation
    marks = []
    for i in range(subjects):
        while True:
            try:
                mark = float(input(f"  Subject {i+1}: "))
                if 0 <= mark <= max_marks:
                    marks.append(mark)
                    break
                else:
                    print(f"    ⚠️  Enter marks between 0 and {max_marks}")
            except ValueError:
                print("    ⚠️  Please enter a valid number")
    
    # Calculate results
    total_obtained = sum(marks)
    total_maximum = subjects * max_marks
    percentage = (total_obtained / total_maximum) * 100
    average = total_obtained / subjects
    
    # Display comprehensive results
    print(f"\n📊 RESULTS")
    print("=" * 30)
    print(f"Total Marks: {total_obtained}/{total_maximum}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Average per Subject: {average:.2f}")
    
    # International grade system
    if percentage >= 90:
        grade = "A+ 🏆 (Outstanding)"
    elif percentage >= 80:
        grade = "A ⭐ (Excellent)" 
    elif percentage >= 70:
        grade = "B 👍 (Very Good)"
    elif percentage >= 60:
        grade = "C ✅ (Good)"
    elif percentage >= 50:
        grade = "D 📈 (Satisfactory)"
    else:
        grade = "F ❌ (Needs Improvement)"
    
    print(f"Grade: {grade}")
    
    return {
        'percentage': percentage,
        'total': total_obtained,
        'grade': grade,
        'average': average
    }

# Call the function
if __name__ == "__main__":
    result = calculate_student_percentage()

