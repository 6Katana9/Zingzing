/** @type {import('next').NextConfig} */
const nextConfig = {
	images: {
		remotePatterns: [
			{
				protocol: 'https',
				hostname: 'zingzing.ru',
				pathname: '/**',
			},
			{
				protocol: 'https',
				hostname: 'zingzing.kz',
				pathname: '/**',
			},
			{
				protocol: 'https',
				hostname: 'zingzing.kg',
				pathname: '/**',
			},
			{
				protocol: 'https',
				hostname: 'zingzing.uz',
				pathname: '/**',
			},

		],
	},
}

export default nextConfig
