/* copyright 2016 Apache 2 sddekit authors */

#include "sddekit.h"

#include <string>
#include <vector>

/**
 * \file sddekit.hpp C++ interface to sddekit.
 *
 */

namespace sd
{
	inline uint32_t ver_major() { return sd_ver_major(); }
	inline uint32_t ver_minor() { return sd_ver_minor(); }

	/* util {{{ */

	inline std::vector<double>
	read_square_matrix(std::string fname)
	{
		uint32_t i, n;
		double *w;
		std::vector<double> out;
		sd_util_read_square_matrix(fname.c_str(), &n, &w);
		for (i=0; i<n; i++)
			out.push_back(w[i]);
		sd_free(w);
		return out;
	}

	inline uint32_t
	uniqi(const uint32_t n, const uint32_t * restrict ints, 
		      uint32_t * restrict nuniq, uint32_t ** restrict uints)
	{
		return sd_util_uniqi(n, ints, nuniq, uints);
	}

	/* util }}} */

} /* namespace sd */

/* vim: foldmethod=marker
 */
