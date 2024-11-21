var myObject = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
      title: 'Your Gym management website, in Sync',
      description:
        'Transform your fitness journey with GymSync – where real-time equipment tracking, personalized plans, and seamless communication come together for an unbeatable gym experience. Stay in sync with your goals, every step of the way.',
      gymLogoUrl: '/static/images/gymlogo.png',
    isHeroImgVisible: false,
    isMainBtnVisible: false,
    },
    mounted() {
    // Wait until the Vue component is mounted and DOM is ready
    this.observeElements();
  },
  methods: {
    observeElements() {
      const heroImg = this.$el.querySelector('.hero-img');
      const mainBtn = this.$el.querySelector('.main-btn');
      
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            if (entry.target === heroImg) {
              this.isHeroImgVisible = true;
            } else if (entry.target === mainBtn) {
              this.isMainBtnVisible = true;
            }
          } else {
            // reset visibility when out of view
            if (entry.target === heroImg) {
              this.isHeroImgVisible = false;
            } else if (entry.target === mainBtn) {
              this.isMainBtnVisible = false;
            }
          }
        });
      }, {
        threshold: 0.1 // Trigger when 10% is visible
      });
  
      observer.observe(heroImg);
      observer.observe(mainBtn);
    }
  }
  });
  
  var testimonialApp = new Vue({
    el: '#testimonialApp',
    delimiters: ['[[', ']]'],
    data: {
        activeIndex: 0, 
        tabs: [
            { img: 'https://livedemo00.template-help.com/wt_62267_v8/prod-20823-one-service/images/testimonials-01-179x179.png' },
            { img: 'https://livedemo00.template-help.com/wt_62267_v8/prod-20823-one-service/images/testimonials-02-306x306.png' },
            { img: 'https://livedemo00.template-help.com/wt_62267_v8/prod-20823-one-service/images/testimonials-03-179x179.png' }
        ],
        testimonials: [
            { quote: 'GymSync web has completely transformed my fitness journey! The personalized training plans and real-time communication with my trainer have helped me stay on track and achieve goals I never thought possible.', name: 'peter lee' },
            { quote: 'The trainers at GymSync are fantastic! Their expertise and the focus on core strength have made a huge difference in my performance. The positive environment keeps me motivated every day!', name: 'john doe' },
            { quote: 'I love how GymSync integrates everything I need—personalized workout plans, easy communication with my trainer, and real-time equipment availability. Its the most efficient and motivating gym experience I ever had!', name: 'sarah smith' }
        ],
        isTitleVisible: false
    },
    mounted() {
        this.observeTitle();
    },
    methods: {
        setActive(index) {
            this.activeIndex = index;
        },
        observeTitle() {
            const title = this.$refs.testimonialTitle;
  
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        this.isTitleVisible = true;
                    } else {
                        this.isTitleVisible = false;
                    }
                });
            }, {
                threshold: 0.1  // Trigger when 10% of the title is visible
            });
  
            observer.observe(title);
        }
    },
    watch: {
        isTitleVisible(newVal) {
            const title = this.$refs.testimonialTitle;
            if (newVal) {
                title.classList.add('visible');
            } else {
                title.classList.remove('visible');
            }
        }
    }
  });