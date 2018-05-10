LIMIT=100;

figure;
hold on;

scatter(sizes(1:LIMIT),insertion(1:LIMIT));
scatter(sizes(1:LIMIT),merge(1:LIMIT));

title('Insertion sort vs. Merge sort');
xlabel('Tamaño de la lista');
ylabel('Tiempo [s]');
legend('Insertion sort','Merge sort','Location','northwest');
