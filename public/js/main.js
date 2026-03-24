document.addEventListener('DOMContentLoaded', () => {
  initQuiz();
  initFaq();
  initNav();
  initStickyAdClose();
});

function initQuiz() {
  const quizCard = document.querySelector('.quiz-card');
  if (!quizCard) return;

  const steps = quizCard.querySelectorAll('.quiz-step');
  const progressFill = quizCard.querySelector('.quiz-progress-fill');
  const loadingView = quizCard.querySelector('.quiz-loading');
  const resultsView = quizCard.querySelector('.quiz-results');
  let currentStep = 0;
  const totalSteps = steps.length;
  const answers = {};

  function showStep(idx) {
    steps.forEach(s => s.classList.remove('active'));
    if (idx < totalSteps) {
      steps[idx].classList.add('active');
      progressFill.style.width = ((idx + 1) / totalSteps * 100) + '%';
    }
  }

  quizCard.querySelectorAll('.quiz-option').forEach(btn => {
    btn.addEventListener('click', () => {
      const step = btn.closest('.quiz-step');
      step.querySelectorAll('.quiz-option').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      answers[currentStep] = btn.dataset.value;

      setTimeout(() => {
        currentStep++;
        if (currentStep >= totalSteps) {
          showLoading();
        } else {
          showStep(currentStep);
        }
      }, 300);
    });
  });

  function showLoading() {
    steps.forEach(s => s.classList.remove('active'));
    progressFill.style.width = '100%';
    if (loadingView) {
      loadingView.style.display = 'block';
      setTimeout(() => {
        loadingView.style.display = 'none';
        if (resultsView) resultsView.style.display = 'block';
      }, 3200);
    }
  }

  showStep(0);
}

function initFaq() {
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.faq-item');
      const wasOpen = item.classList.contains('open');
      item.closest('.faq-list').querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!wasOpen) item.classList.add('open');
    });
  });
}

function initNav() {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => links.classList.toggle('open'));
  }
}

function initStickyAdClose() {
  document.querySelectorAll('.ad-close').forEach(btn => {
    btn.addEventListener('click', () => {
      btn.closest('.ad-sticky-footer').style.display = 'none';
    });
  });
}
