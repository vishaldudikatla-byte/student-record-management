#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to store student details
struct Student {
    int rollNo;
    char name[50];
    float marks;
    struct Student *next;
};

// Head pointer for linked list
struct Student *head = NULL;

// Function to add a student record
void addStudent(int rollNo, char name[], float marks) {
    struct Student *newStudent = (struct Student*)malloc(sizeof(struct Student));
    newStudent->rollNo = rollNo;
    strcpy(newStudent->name, name);
    newStudent->marks = marks;
    newStudent->next = head;
    head = newStudent;
    printf("\n✅ Record added successfully!\n");
}

// Function to display all records
void displayStudents() {
    struct Student *temp = head;
    if (temp == NULL) {
        printf("\n⚠️ No student records found!\n");
        return;
    }
    printf("\n📘 Student Records:\n");
    printf("--------------------------------------------\n");
    printf("%-10s %-20s %-10s\n", "Roll No", "Name", "Marks");
    printf("--------------------------------------------\n");
    while (temp != NULL) {
        printf("%-10d %-20s %-10.2f\n", temp->rollNo, temp->name, temp->marks);
        temp = temp->next;
    }
    printf("--------------------------------------------\n");
}

// Function to delete a student record
void deleteStudent(int rollNo) {
    struct Student *temp = head, *prev = NULL;
    if (temp == NULL) {
        printf("\n⚠️ No records to delete!\n");
        return;
    }

    while (temp != NULL && temp->rollNo != rollNo) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("\n❌ Student with Roll No %d not found!\n", rollNo);
        return;
    }

    if (prev == NULL)
        head = temp->next;
    else
        prev->next = temp->next;

    free(temp);
    printf("\n🗑️ Record deleted successfully!\n");
}

// Function to search for a student
void searchStudent(int rollNo) {
    struct Student *temp = head;
    while (temp != NULL) {
        if (temp->rollNo == rollNo) {
            printf("\n✅ Record Found:\n");
            printf("Roll No: %d\n", temp->rollNo);
            printf("Name: %s\n", temp->name);
            printf("Marks: %.2f\n", temp->marks);
            return;
        }
        temp = temp->next;
    }
    printf("\n❌ Student with Roll No %d not found!\n", rollNo);
}

// Main function
int main() {
    int choice, rollNo;
    char name[50];
    float marks;

    while (1) {
        printf("\n==============================");
        printf("\n Student Record Management ");
        printf("\n==============================");
        printf("\n1. Add Student");
        printf("\n2. Display Students");
        printf("\n3. Search Student");
        printf("\n4. Delete Student");
        printf("\n5. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("\nEnter Roll No: ");
                scanf("%d", &rollNo);
                printf("Enter Name: ");
                scanf(" %[^\n]s", name);
                printf("Enter Marks: ");
                scanf("%f", &marks);
                addStudent(rollNo, name, marks);
                break;

            case 2:
                displayStudents();
                break;

            case 3:
                printf("\nEnter Roll No to search: ");
                scanf("%d", &rollNo);
                searchStudent(rollNo);
                break;

            case 4:
                printf("\nEnter Roll No to delete: ");
                scanf("%d", &rollNo);
                deleteStudent(rollNo);
                break;

            case 5:
                printf("\n👋 Exiting program... Goodbye!\n");
                exit(0);

            default:
                printf("\n⚠️ Invalid choice! Try again.\n");
        }
    }

    return 0;
}