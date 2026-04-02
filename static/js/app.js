document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('client-form');
    const programSelect = document.getElementById('program');
    const progressInput = document.getElementById('progress');
    const adherenceVal = document.getElementById('adherence-val');
    const weightInput = document.getElementById('weight');
    const resetBtn = document.getElementById('reset-btn');
    
    const emptyState = document.getElementById('empty-state');
    const detailsContent = document.getElementById('details-content');
    const calorieTarget = document.getElementById('calorie-target');
    const workoutPlan = document.getElementById('workout-plan');
    const dietPlan = document.getElementById('diet-plan');
    const saveStatus = document.getElementById('save-status');

    let currentProgramData = null;

    // Update range display
    progressInput.addEventListener('input', (e) => {
        adherenceVal.textContent = e.target.value;
    });

    // Handle program selection
    programSelect.addEventListener('change', async (e) => {
        const programId = e.target.value;
        if (!programId) return;

        try {
            const response = await fetch(`/api/program/${programId}`);
            if (!response.ok) throw new Error('Program not found');
            
            currentProgramData = await response.json();
            
            // Show details
            emptyState.classList.add('hidden');
            detailsContent.classList.remove('hidden');

            // Apply specific color to style
            document.documentElement.style.setProperty('--accent', currentProgramData.color);

            // Update content
            workoutPlan.textContent = currentProgramData.workout;
            dietPlan.textContent = currentProgramData.diet;

            updateCalories();
        } catch (error) {
            console.error('Error fetching program:', error);
        }
    });

    // Handle weight change for calorie calculation
    weightInput.addEventListener('input', updateCalories);

    function updateCalories() {
        if (currentProgramData && weightInput.value > 0) {
            const weight = parseFloat(weightInput.value);
            const calories = Math.round(weight * currentProgramData.calorie_factor);
            calorieTarget.textContent = `${calories} kcal / day`;
        } else {
            calorieTarget.textContent = '-- kcal / day';
        }
    }

    // Handle form submit
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        saveStatus.classList.remove('hidden');
        setTimeout(() => {
            saveStatus.classList.add('hidden');
        }, 3000);
    });

    // Handle reset
    resetBtn.addEventListener('click', () => {
        adherenceVal.textContent = '0';
        emptyState.classList.remove('hidden');
        detailsContent.classList.add('hidden');
        document.documentElement.style.setProperty('--accent', 'var(--primary)');
        currentProgramData = null;
        saveStatus.classList.add('hidden');
    });
});
