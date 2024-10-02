var myObject = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
      title: 'Your Gym management website, in Sync',
      description:
        'Welcome to Gravity Health Club, where fitness meets innovation. Our cutting-edge facility in North Delhi offers personalized training, state-of-the-art equipment, and a supportive community to help you reach your goals. Join us and defy gravity on your journey to a healthier, happier you.',
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
            { quote: 'I have tried a lot of food delivery services but Plate is something out of this world! Their food is really healthy and it tastes great, which is why I recommend this company to all my friends!', name: 'peter lee' },
            { quote: 'The quality of service and professionalism provided by the team is truly commendable!', name: 'john doe' },
            { quote: 'An amazing experience, truly worth every penny. I recommend it to all my colleagues!', name: 'sarah smith' }
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