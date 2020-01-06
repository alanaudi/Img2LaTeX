<template lang='pug'>
#app
  h1 {{ site  }}
</template>

<script>
import axios from 'axios'
import 'babel-polyfill' // for async/await
import 'semantic-ui-offline/semantic.min.css'
export default {

  beforeDestory() {
    document.removeEventListener('keyup', this.key)
  },

  created() {
    document.addEventListener('keyup', this.key)
    this.latestDay()
    this.listDay()
  },

  computed: {
    condition() {
      return (!this.page || 'search' == this.page)
    },
  },

  data() { return {
    site: 'Img2LaTeX',
  }},

  methods: {
    async correlatedTerms() { if ('' == this.terms)
        return
      this.searching = true
      this.encodeStr = encodeURIComponent(this.terms)
      const { data } = await axios.get(`/correlate/${this.encodeStr}/${this.boards}/${this.searchingWeek}/${this.searchingWeek}`)
	    this.correlate_table = data
      this.page = 'correlate'
      this.results = []
	  this.termsCorrelate = this.terms
      this.searching = false
    },
  },
}
</script>

<style lang="sass">
a
  cursor: pointer
tr
  h1
    text-align: center
</style>

