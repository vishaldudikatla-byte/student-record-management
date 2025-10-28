
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
